from django.db import models
from model_utils.models import TimeStampedModel
from artists.models import Artist
from django.utils import timezone


# Create your models here.
class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='New Album')
    release_date = models.DateTimeField('release date')
    cost = models.FloatField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

