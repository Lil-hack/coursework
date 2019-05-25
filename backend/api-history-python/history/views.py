from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework import permissions, renderers, viewsets, status
from rest_framework.decorators import detail_route, action, list_route
from rest_framework.response import Response

from history.models import History

from history.serializers import HistorySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    permission_classes = (

     )

    @action(methods=['get'], detail=True, url_path='list/(?P<page>[0-9]+)')
    def listAll(self, request,*args, **kwargs):
        # find all categories first

        # then, filter the categories itself.

        metka=False
        for item in kwargs.values():
            if metka == False:
                uuid=item
            else:
                page=item
            metka=True

        if int(page)==0:
            return Response('[]',status=status.HTTP_204_NO_CONTENT)
        queryset = History.objects.filter(user_uuid=uuid).order_by('-created')
        paginator = Paginator(queryset, 10)

        if int(page)>paginator.num_pages:
            return Response('[]',status=status.HTTP_204_NO_CONTENT)
        queryset = History.objects.filter(user_uuid=uuid).order_by('-created')
        serializer = HistorySerializer(paginator.get_page(page), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




    def perform_create(self, serializer):
        serializer.save()



