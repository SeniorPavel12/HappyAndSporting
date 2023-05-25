from rest_framework.routers import SimpleRouter

from music.api.viewsets.viewset import MusicViewSet, PlaylistViewSet

router = SimpleRouter()
router.register('music', MusicViewSet, basename='music')
router.register('playlist', PlaylistViewSet, basename='playlist')

urlpatterns = []
urlpatterns += router.urls
