from rest_framework.routers import SimpleRouter

from imageupload.views import ImagesViewSet

router = SimpleRouter()

router.register('images', ImagesViewSet, basename='images')

urlpatterns = router.urls