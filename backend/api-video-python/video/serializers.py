from django.contrib.auth.models import User
from rest_framework import serializers

from video.models import Video, Photo


class VideoSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
        model = Video
        fields = ('id',  'created', 'title', 'description','preview')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title')   # <-- HERE
