import io
import os
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


from frame.models import Frame, Photo

from frame.serializers import FrameSerializer, PhotoSerializer


import cv2, pafy
import numpy as np
import time
import youtube_dl

import pytube

def video_process(name):
    file_name = download_video('https://www.youtube.com/watch?v={0}'.format(name))

    mass_hash = video_to_pHash('/app/{0}'.format(file_name), name)

    delete_video(file_name)

    objs = [
        Frame(
            video_uuid=e['uuid'],
            hash=e['hash'],
            frame=e['frame']
        )
        for e in mass_hash
    ]

    Frame.objects.bulk_create(objs)

    return True

def download_video(url):

    # Определяем путь к папке
    SAVE_PATH ='/app/'
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(SAVE_PATH)

    return stream.default_filename

def delete_video(file_name):


    try:
        os.remove('/app/{0}'.format(file_name))
    except OSError:
       print(OSError)

    return

def video_to_pHash(video_name, uuid):
    """

    :rtype: object
    """
    cap = cv2.VideoCapture(video_name)
    keys = 'uuid', 'hash', 'frame'
    mas_hash = []
    i=0
    while True:
        i=i+1
        ret, frame = cap.read()

        if not ret:
            break
        img = Image.fromarray(frame)
        hash = imagehash.phash(img, 8)

        values=uuid,str(hash),i
        video_item = dict(zip(keys, values))

        metka = False

        for item in reversed(mas_hash):
            if item['hash'] == str(hash):
                metka = True
                break
        if metka == False:
            mas_hash.append(video_item)

    np_data = np.asarray(mas_hash)

    return np_data
#print(get_photo_fromYT("https://www.youtube.com/watch?v=helu9J9uf9Y",500))
class FrameViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Frame.objects.all()
    serializer_class = FrameSerializer

    permission_classes = (

     )

    @action(methods=['get'], detail=False, url_path='search/(?P<name>.+)')
    def search(self, request,*args, **kwargs):
        # find all categories first

        # then, filter the categories itself.


        for item in kwargs.values():
            name=item

        # video_process('OorBMN28n7o')
        video_process(name)
        print('i end ready')


        return Response('7', status=status.HTTP_200_OK)

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



        data = request.FILES['filename'].file
        out_image = Image.open(data)

        # хэщ из фото
        hash = imagehash.phash(out_image, 8)


        # найти id видео  и номер кадра
        print(hash)



        return Response(str(hash), status=status.HTTP_200_OK)