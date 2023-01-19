from .models import Images
from .serializers import ImagesSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.order_by('id')
    serializer_class = ImagesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()
