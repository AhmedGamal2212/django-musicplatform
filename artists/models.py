from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(max_length=255, unique=True)
    social_link = models.URLField(max_length=254, null=False, blank=True)

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ['stage_name']
