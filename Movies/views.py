from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class WatchListAV(APIView):
    def get(self, request):
        watchlists = WatchList.objects.all()
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        watchlist = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        watchlist = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        watchlist = get_object_or_404(WatchList, pk=pk)
        watchlist.delete()
        return Response({"msg": "model deleted"}, status=status.HTTP_200_OK)


class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        platform.delete()
        return Response({"msg": "model deleted"}, status=status.HTTP_200_OK)
