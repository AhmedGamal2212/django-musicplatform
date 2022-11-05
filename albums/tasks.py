from celery import shared_task
from django.core.mail import send_mail

from artists.models import Artist
from musicplatform import settings


@shared_task(bind=True)
def send_congratulations_mail(self, album_name, artist_name):
    mail_subject = 'Congratulations!'
    artist = Artist.objects.get(stage_name=artist_name)
    message = f"Hi {artist_name}, Congratulations on the new album!.\nYou have successfully created a new album: {album_name}"
    to_email = artist.user.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return "Done"
