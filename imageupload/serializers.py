from rest_framework import serializers
from .models import Images

class ImagesSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Images
        fields = ['id', 'title','orginal_name_file', 'width', 'height', 'image_url']
        extra_kwargs = {
            'orginal_name_file': {'read_only': True}
        }

