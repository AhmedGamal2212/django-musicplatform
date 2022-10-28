from django.db import models
from django.utils.text import slugify
from model_utils.models import TimeStampedModel
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='New Album')
    release_date = models.DateTimeField('release date')
    cost = models.FloatField(blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.SlugField(default=None, blank=True)
    image = models.ImageField(upload_to='song-images', blank=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG',
                               options={'quality': 60})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name is None or not len(self.name):
            self.name = slugify(self.album.name)
            self.save()
        super(Song, self).save(*args, **kwargs)
