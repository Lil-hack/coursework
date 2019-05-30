import io
import uuid
from io import StringIO
import imagehash
from PIL import Image
import boto3
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import permissions, renderers, viewsets, status
from rest_framework.decorators import detail_route, action, list_route
from rest_framework.response import Response
import django.contrib.postgres
from video.models import Video, Photo

from video.serializers import VideoSerializer, PhotoSerializer


import cv2, pafy
import numpy as np
import time
import youtube_dl

def get_photo_fromYT(url, frame2):
    url = "https://www.youtube.com/watch?v=seI9H18ZvgE"
    # videoPafy = pafy.new(url)
    # best = videoPafy.getbest()
    # print(url)
    # print(videoPafy)
    # print(best)
    # cap = cv2.VideoCapture(best.url)
    # print(cap)
    # # cap.set(25, frame2)
    # print(frame2)
    # print(cap.isOpened())
    # ret, frame = cap.read()
    # print(ret)
    # # is_success, buffer = cv2.imencode(".jpg", frame)
    # # io_buf = io.BytesIO(buffer)
    # print(frame)

    video = pafy.new(url)
    best = video.getbest(preftype="webm")
    video = cv2.VideoCapture(best.url)
    print(video.isOpened())
    return 'lox'

#print(get_photo_fromYT("https://www.youtube.com/watch?v=helu9J9uf9Y",500))
class VideoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    permission_classes = (

     )

    @action(methods=['get'], detail=False, url_path='search/(?P<name>.+)')
    def search(self, request,*args, **kwargs):
        # find all categories first

        # then, filter the categories itself.


        for item in kwargs.values():
            name=item


        queryset = Video.objects.filter(Q(title__icontains=name) | Q(description__icontains=name))
        paginator = Paginator(queryset, 20)
        serializer = VideoSerializer(paginator.get_page(1), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=False, methods=['put'], name='Uploader View')
    # def uploader(self, request, filename):
    #     # Parsed data will be returned within the request object by accessing 'data' attr
    #
    #     data = request.FILES['filename']
    #     # print(data.read())
    #     path = default_storage.save('tmp/somename.jpg', ContentFile(data.read()))
    #     print(path)
    #     im = Image.open(path)
    #
    #     return Response(status=204)

    def perform_create(self, serializer):
        serializer.save()



class PhotoViewSet(viewsets.ViewSet):


    @action(detail=False, methods=['post'], name='Upload View')
    def upload(self, request, filename):
        # Parsed data will be returned within the request object by accessing 'data' attr


        s3=boto3.resource('s3',
                            aws_access_key_id='AKIAURXICIFTQBXRYYVL',
                            aws_secret_access_key='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')

        for bucket in s3.buckets.all():
            bucket_name=bucket.name

        #загрузка фото
        data = request.FILES['filename'].file
        out_image = Image.open(data)

        # хэщ из фото
        hash = imagehash.phash(out_image, 8)

        #загрузить на с3
        image = io.BytesIO()
        out_image.save(image, "JPEG")
        image.seek(0)
        file_name='image_from_user_{0}.jpg'.format(uuid.uuid4())
        s3.Bucket(bucket_name).put_object(Key=file_name,  Body=image)
        bucket_location = s3.meta.client.get_bucket_location(Bucket=bucket_name)
        object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            bucket_location['LocationConstraint'],
            bucket_name,
            file_name)

        # найти id видео  и номер кадра
        print(hash)

        # получить картинку из кадра и сохранить на с3
        out_image = get_photo_fromYT("https://www.youtube.com/watch?v=helu9J9uf9Y", 500)
        # image = io.BytesIO()
        # out_image.save(image, "JPEG")
        # image.seek(0)
        # cv2.imwrite('test.jpg', out_image)


        # file_name='image_from_search_{0}.jpg'.format(uuid.uuid4())
        # s3.Bucket(bucket_name).put_object(Key=file_name, Body=out_image)
        #
        # bucket_location = s3.meta.client.get_bucket_location(Bucket=bucket_name)
        # object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        #     bucket_location['LocationConstraint'],
        #     bucket_name,
        #     file_name)

        return Response(str(object_url), status=status.HTTP_200_OK)