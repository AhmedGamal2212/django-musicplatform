from django.db import models
from django.utils.text import slugify
from model_utils.models import TimeStampedModel
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from albums.validators import validators
from .tasks import send_congratulations_mail


# Create your models here.

class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='New Album')
    release_date = models.DateTimeField('release date', blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        send_congratulations_mail(self.name, self.artist.stage_name)
        super(Album, self).save(*args, **kwargs)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.SlugField(default=None, blank=True)
    image = models.ImageField(upload_to='song-images')
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG',
                               options={'quality': 60})
    audio_file = models.FileField(upload_to='music', validators=[validators.validate_audio])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name is None or not len(self.name):
            self.name = slugify(self.album.name)
            self.save()
        super(Song, self).save(*args, **kwargs)
