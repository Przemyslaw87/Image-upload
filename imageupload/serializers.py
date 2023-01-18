from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'title', 'width', 'height', 'image_url']

