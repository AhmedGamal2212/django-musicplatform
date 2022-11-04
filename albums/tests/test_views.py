import string
import django.utils.datastructures
import pytest
from rest_framework.test import APIClient
from artists.serializers import ArtistSerializer


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


@pytest.mark.django_db
def test_create_album_with_null_field(auth_client):
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
    with pytest.raises(django.utils.datastructures.MultiValueDictKeyError):
        response = client.post('/albums/', {
            'cost': '100',
            'is_approved': 'true'
        })
        assert response.status_code == 500


@pytest.mark.django_db
def test_album_create_with_no_provided_name(auth_client):
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
        'name': '',
        'cost': '100',
        'is_approved': 'true'
    })
    assert response.status_code == 200
    data = response.data
    assert data['name'] == 'New Album'


def create_an_artist(client):
    client.post('/artists/', {
        'stage_name': 'El_Tester',
        'social_link': 'https://testing.com'
    })


def create_approved_albums(client):
    price = 1
    for c in string.ascii_lowercase:
        client.post('/albums/', {
            'name': f'{c}',
            'is_approved': 'true',
            'cost': f'{price}'
        })
        price += 2


def create_not_approved_albums(client):
    price = 1
    for c in string.ascii_lowercase:
        client.post('/albums/', {
            'name': f'{c}{c}',
            'is_approved': 'false',
            'cost': f'{price}'
        })
        price += 2


@pytest.mark.django_db
def test_manual_filtered_list_request_unauthenticated(auth_client):
    temp_client = auth_client()
    create_an_artist(temp_client)
    create_approved_albums(temp_client)
    create_not_approved_albums(temp_client)
    client = APIClient()
    response = client.get('/albums/manual/')

    assert response.status_code == 200
    data = response.data
    assert 'count' in data
    assert data['count'] == 26
    for album in data['results']:
        assert album['is_approved']
        assert album['artist'] == {
            'id': 1,
            'stage_name': 'El_Tester',
            'social_link': 'https://testing.com'
        }


@pytest.mark.django_db
def test_manual_filtered_list_request_invalid_limit_datatype(auth_client):
    client = auth_client()
    create_an_artist(client)
    create_approved_albums(client)
    create_not_approved_albums(client)
    response = client.get('/albums/manual/?limit=test/')
    assert response.status_code == 400
    assert response.data['details'] == 'Cost and limit queries must be only numbers.'


@pytest.mark.django_db
def test_manual_filtered_list_request_invalid_cost__lte__datatype(auth_client):
    client = auth_client()
    create_an_artist(client)
    create_approved_albums(client)
    create_not_approved_albums(client)
    response = client.get('/albums/manual/?cost__lte=test/')
    assert response.status_code == 400
    assert response.data['details'] == 'Cost and limit queries must be only numbers.'


@pytest.mark.django_db
def test_manual_filtered_list_request_invalid_cost__gte__datatype(auth_client):
    client = auth_client()
    create_an_artist(client)
    create_approved_albums(client)
    create_not_approved_albums(client)
    response = client.get('/albums/manual/?cost__gte=test/')
    assert response.status_code == 400
    assert response.data['details'] == 'Cost and limit queries must be only numbers.'


@pytest.mark.django_db
def test_manual_filtered_list_request_cost__lte(auth_client):
    client = auth_client()
    create_an_artist(client)
    create_approved_albums(client)
    create_not_approved_albums(client)
    response = client.get('/albums/manual/?cost__lte=10')
    assert response.status_code == 200
    data = response.data
    assert data['count'] == 5
    for album in data['results']:
        assert album['cost'] <= 10.0


@pytest.mark.django_db
def test_manual_filtered_list_request_cost__lte(auth_client):
    client = auth_client()
    create_an_artist(client)
    create_approved_albums(client)
    create_not_approved_albums(client)
    response = client.get('/albums/manual/?cost__gte=10')
    assert response.status_code == 200
    data = response.data
    assert data['count'] == 21
    for album in data['results']:
        assert album['cost'] >= 10
