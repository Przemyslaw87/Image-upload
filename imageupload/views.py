from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Images
from .serializers import ImagesSerializer


class ImagesFilter(filters.FilterSet):
    """
    A filter set for the Images model.

    This filter set can be used to filter the queryset of Images based on the title field.

    Attributes:
        title (CharFilter): A filter that searches for images whose title contains a certain string.
    """

    title = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        fields = "title"


class ImagesViewSet(viewsets.ModelViewSet):
    """
    A viewset for the Images model.

    This viewset provides the CRUD functionality for the Images model.
    It uses the ImagesSerializer to handle the serialization and deserialization of the Images model instances.
    And it uses ImagesFilter to filter the queryset of Images based on the title field.

    Attributes:
        queryset (QuerySet): The queryset of Images to be used for the viewset.
        serializer_class (ImagesSerializer): The serializer class to be used for the viewset.
        filterset_class (ImagesFilter): The filterset class to be used for the viewset.
        parser_classes (MultiPartParser, FormParser): The parser classes to be used for the viewset.
    """

    queryset = Images.objects.order_by("id")
    serializer_class = ImagesSerializer
    filterset_class = ImagesFilter
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save_and_upload()
