from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets, status
from rest_framework.decorators import detail_route, action
from rest_framework.response import Response

from users.models import Users

from users.serializers import UsersSerializer
import hashlib


def make_password(password):
    assert password
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hash

def check_password(hash, password):
    """Generates the hash for a password and compares it."""
    generated_hash = make_password(password)
    return hash == generated_hash


class UsersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    permission_classes = (

     )



    @action(methods=['get'],detail=False,url_path='login/(?P<username>.+)(?P<password>.+)')
    def login(self, request, *args, **kwargs):
        self.lookup_field = 'username'
        self.lookup_url_kwarg = 'username'
        users = self.get_object()
        if check_password(users.password,kwargs.get(0)):
            print(users)
        serializer = UsersSerializer(users)
        return Response(serializer.data)



    def perform_create(self, serializer):
        serializer.save()



