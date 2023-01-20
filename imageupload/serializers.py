from rest_framework import serializers
from .models import Images

class ImagesSerializer(serializers.ModelSerializer):
    """
       A serializer for the Images model.
    """
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Images
        fields = ['id', 'title', 'original_name_file', 'width', 'height', 'image_url']
        extra_kwargs = {
            'original_name_file': {'read_only': True}
        }

