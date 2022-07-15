from rest_framework import serializers
from example.models import Image, Image_URL

class ImSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_URL
        feilds = "__all__"