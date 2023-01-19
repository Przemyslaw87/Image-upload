from rest_framework import serializers
from .models import Images

class ImagesSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Images
        fields = ['id', 'title', 'width', 'height', 'image_url']

