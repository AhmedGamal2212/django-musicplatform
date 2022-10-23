from django.db import models


# TODO: order by approved albums.
# class ArtistManager(models.Manager):
#     def get_query_set(self):
#         params = self.request.query_params
#         if params.contains('approved_albums'):
#             return super().get_queryset().filter(is_approved=True).count()

class Artist(models.Model):
    stage_name = models.CharField(max_length=255, unique=True)
    social_link = models.URLField(max_length=254, null=False, blank=True)

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ['stage_name']
