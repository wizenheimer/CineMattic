from rest_framework import serializers
from .models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        # fields = ["id", "name", "description", "rating"]
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        models = StreamPlatform
        fields = "__all__"
