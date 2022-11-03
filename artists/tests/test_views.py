import pytest
from rest_framework.test import APIClient
from artists.models import Artist


def perform_get(client):
    artist = Artist.objects.create(
        stage_name='testing from pytest',
        social_link='https://google.com'
    )
    response = client.get('/artists/')
    assert response.status_code == 200
    assert len(response.data) == Artist.objects.all().count()
    assert response.data[0]['id'] == artist.id


@pytest.mark.django_db
def test_get_artists_unauthorized():
    client = APIClient()
    perform_get(client)


@pytest.mark.django_db
def test_get_artists_authorized(auth_client):
    client = auth_client()
    perform_get(client)


@pytest.mark.django_db
def test_create_artist_unauthorized():
    client = APIClient()
    response = client.post('/artists/', {
        'stage_name': 'ahmed gamal',
        'social_link': 'https://google.com'
    })
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_artist_authorized(auth_client):
    client = auth_client()
    response = client.post('/artists/', {
        'stage_name': 'ahmed gamal',
        'social_link': 'https://google.com'
    })
    assert response.status_code == 201
    assert response.data['stage_name'] == 'ahmed gamal'
    assert response.data['social_link'] == 'https://google.com'


# @pytest.mark.django_db
# def test_anything(auth_client):
#     client = auth_client()
#     response = client.post('/artists/', {
#         'stage_name': 'ahmed gamal',
#         'social_link': 'https://google.com'
#     })
#     res = client.get('/users/1/').GET
#     assert res == 2
