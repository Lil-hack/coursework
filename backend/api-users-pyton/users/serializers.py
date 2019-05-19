from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Users


class UsersSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
        model = Users
        fields = ('uuid', 'username',  'first_name', 'last_name','email','password')



