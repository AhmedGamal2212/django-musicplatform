import pytest
from rest_framework.test import APIClient
from artists.models import Artist


@pytest.mark.django_db
def test_get_artists(auth_client):
    unauthenticated_client = APIClient()
    authenticated_client = auth_client()
    authenticated_client.post('/artists/', {
        'stage_name': 'Tester',
        'social_link': 'https://tester.com'
    })

    response = unauthenticated_client.get('/artists/')
    data = response.data
    assert response.status_code == 200
    assert len(data) == 1
    artist = data[0]
    assert artist['stage_name'] == 'Tester'
    assert artist['social_link'] == 'https://tester.com'
    assert 'id' in artist


@pytest.mark.django_db
def test_create_artist_unauthenticated():
    client = APIClient()
    response = client.post('/artists/', {
        'stage_name': 'Tester',
        'social_link': 'https://tester.com'
    })
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_artist_authenticated_with_no_prior_artist(auth_client):
    client = auth_client()
    response = client.post('/artists/', {
        'stage_name': 'Tester',
        'social_link': 'https://tester.com'
    })
    assert response.status_code == 200
    data = response.data
    assert 'id' in data
    assert data['stage_name'] == 'Tester'
    assert data['social_link'] == 'https://tester.com'


# @pytest.mark.django_db
# def test_anything(auth_client):
#     client = auth_client()
#     response = client.post('/artists/', {
#         'stage_name': 'ahmed gamal',
#         'social_link': 'https://google.com'
#     })
#     res = client.get('/users/1/').GET
#     assert res == 2
