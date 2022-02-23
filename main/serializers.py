from rest_framework import serializers
from .models import MapImage

class MapImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapImage
        fields = ["ground_flour", "first_flour", "second_flour"]