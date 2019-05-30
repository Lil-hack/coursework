from django.contrib.auth.models import User
from rest_framework import serializers

from frame.models import Frame, Photo


class FrameSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
        model = Frame
        fields = ('video_uuid', 'hash', 'frame')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title')   # <-- HERE
