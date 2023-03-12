from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=250)
    about = models.CharField(max_length=250)
    website = models.URLField(max_length=300)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=250)
    story = models.CharField(max_length=450)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(
        StreamPlatform,
        on_delete=models.CASCADE,
        related_name="watchlist",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
