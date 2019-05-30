from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from video import views

# Create a router and register our viewsets with it.
from video.views import PhotoViewSet, VideoViewSet

router = DefaultRouter()
router.register(r'video', views.VideoViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^search/upload/(?P<filename>[^/]+)$', PhotoViewSet.as_view({'post': 'upload'}), name='posts_uploader'),
    url(r'^', include(router.urls))
]
