from .models import Image
from .serializers import ImageSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.order_by('id')
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()
