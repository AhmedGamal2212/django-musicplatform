from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from artists.models import Artist
from musicplatform import settings


@shared_task(bind=True)
def send_congratulations_mail(self, album_name, artist_name):
    mail_subject = 'Congratulations!'
    artist = Artist.objects.get(stage_name=artist_name)
    message = f'Hi {artist_name}, Congratulations on the new album!.\nYou have successfully created a new album: {album_name}'
    to_email = artist.user.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return 'Sent'


@shared_task(bind=True)
def check_for_added_albums(self):
    all_artists = Artist.objects.all()
    not_active = []
    for artist in all_artists:
        if artist.album_set.count():
            latest_album = artist.album_set.latest('created')
            if timezone.now() - latest_album.release_date >= timezone.timedelta(days=30):
                not_active.append(artist)

    for artist in not_active:
        mail_subject = 'Warning!'
        artist = Artist.objects.get(stage_name=artist.stage_name)
        message = f'''
            Hi {artist.stage_name}, We noticed that you have not created any new album in the last 30 days,
            the continuous inactivity will cause your popularity on the platform to decrease.
         '''
        to_email = artist.user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return 'Sent'
