from rest_framework import serializers


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("name length must be at least 2 characters")
