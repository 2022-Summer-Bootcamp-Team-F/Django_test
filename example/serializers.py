from rest_framework import serializers
from example.models import Image

class ImSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"