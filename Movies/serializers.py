from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    rating = serializers.DecimalField(decimal_places=1, max_digits=1)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.save()
        return instance
