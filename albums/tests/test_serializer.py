import pytest
from albums.serializers import AlbumSerializer
from users.models import CustomUser
from artists.models import Artist
from albums.models import Album
from artists.serializers import ArtistSerializer


@pytest.mark.django_db
def test_serialization():
    user = CustomUser.objects.create_user(
        username='Tester',
        password='Testing128*',
        email='testing@testing.com',
        bio='anything'
    )
    artist = Artist.objects.create(
        stage_name='El_Tester',
        social_link='https://tester.com',
        user=user
    )
    album = Album.objects.create(
        name='testing_album',
        cost='10',
        is_approved=True,
        artist=artist
    )

    serializer = AlbumSerializer(album)

    keys_set = {'id', 'artist', 'name', 'release_date', 'cost', 'is_approved'}
    data = serializer.data
    assert keys_set == set(data.keys())
    assert data['artist'] == ArtistSerializer(artist).data
    assert data['name'] == album.name
    assert data['release_date'] is None
    assert data['cost'] == float(album.cost)
    assert data['is_approved']
