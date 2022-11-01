import pytest
from rest_framework.test import APIClient
from artists.models import Artist


@pytest.mark.django_db
def test_get_users_unauthorized():
    client = APIClient()
    artist = Artist.objects.create(
        stage_name='testing from pytest',
        social_link='https://google.com'
    )
    response = client.get('/artists/')

    assert response.status_code == 200
    assert len(response.data) == Artist.objects.all().count()
    assert response.data[0]['id'] == artist.id


def test_get_users_authorized(auth_client):
    client = auth_client()
