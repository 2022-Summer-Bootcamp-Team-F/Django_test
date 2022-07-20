from rest_framework import serializers
from ehlfk.models import Image_URL

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_URL
        fields = ['image_id', 'image_url']
        