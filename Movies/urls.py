from django.urls import path

from .views import WatchDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watchlist"),
    path("list/<int:pk>/", WatchDetailAV.as_view(), name="watchlist_detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream"),
    path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name="stream_detail"),
]
