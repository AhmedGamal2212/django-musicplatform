import math
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_album_create_unauthenticated():
    client = APIClient()
    response = client.post('/albums/', {
        'name': 'testing_album',
        'cost': '100',
        'is_approved': 'true'
    })
    assert response.status_code == 401


@pytest.mark.django_db
def test_album_create_user_is_not_an_artist(auth_client):
    client = auth_client()
    response = client.post('/albums/', {
        'name': 'testing_album',
        'cost': '100',
        'is_approved': 'true'
    })
    assert response.status_code == 403


@pytest.mark.django_db
def test_album_create_user_is_an_artist(auth_client):
    client = auth_client()
    response = client.post('/artists/', {
        'stage_name': 'El_Tester',
        'social_link': 'https://testing.com'
    })
    artist = response.data
    response = client.post('/albums/', {
        'name': 'testing_album',
        'cost': '100',
        'is_approved': 'true'
    })
    assert response.status_code == 200
    data = response.data
    assert data['artist'] == artist
    assert 'id' in data
    assert data['is_approved'] is True
    assert data['name'] == 'testing_album'
    assert data['cost'] == float(100)
    assert data['release_date'] is None


@pytest.mark.django_db
def test_album_create_with_duplicated_name(auth_client):
    client = auth_client()
    client.post('/artists/', {
        'stage_name': 'El_Tester',
        'social_link': 'https://testing.com'
    })
    client.post('/albums/', {
        'name': 'testing_album',
        'cost': '100',
        'is_approved': 'true'
    })
    response = client.post('/albums/', {
        'name': 'testing_album',
        'cost': '100',
        'is_approved': 'true'
    })
    assert response.status_code == 400
    assert response.data['details'] == 'You already have an album with the same name.'


# @pytest.mark.django_db
# def test_create_album

# @pytest.mark.django_db
# def test_manual_filtered_list_request_unauthenticated():
#     client = APIClient()
#     response = client.get('/albums/manual/')
#
#     assert response.status_code == 200
#     data = response.data
#     assert 'count' in data
#     assert data['count'] == math.ceil()
