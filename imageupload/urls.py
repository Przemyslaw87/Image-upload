from rest_framework.routers import SimpleRouter

from imageupload.views import ImageViewSet

router = SimpleRouter()

router.register('images', ImageViewSet, basename='images')

urlpatterns = router.urls