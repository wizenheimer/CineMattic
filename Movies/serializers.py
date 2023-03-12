from rest_framework import serializers
from .models import Movie
from .validator import name_length


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250, validators=[name_length])
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

    def validate_name(self, value):
        if len(value) < 2:
            return serializers.ValidationError("Name's too short")
        else:
            return value

    def validate(self, attrs):
        if attrs["name"] == attrs["description"]:
            raise serializers.ValidationError("Name and description shouldn't be same")
        return attrs
