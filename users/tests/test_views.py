import pytest
from rest_framework.test import APIClient
from users.models import CustomUser


# testing users list view


@pytest.mark.django_db
def test_list_view():
    client = APIClient()
    response = client.get('/users/')
    assert response.status_code == 200
    client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'testing@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'bio'
    })
    client.post('/authentication/register/', {
        'username': 'ahmed',
        'email': 'testing2@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'bio'
    })
    response = client.get('/users/')
    assert response.status_code == 200
    assert len(response.data) == 2
    user = response.data[0]
    assert user['username'] == 'gemmy'
    assert user['email'] == 'testing@testing.com'
    assert 'password' not in response.data[0]
    assert user['bio'] == 'bio'


@pytest.mark.django_db
def test_get_user_unauthenticated():
    client = APIClient()
    first_response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'testing@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'bio'
    })
    second_response = client.get('/users/1/')
    first_data, second_data = first_response.data, second_response.data
    assert first_response.status_code == 200 and second_response.status_code == 200
    assert first_data['user']['username'] == second_data['username']
    assert first_data['user']['email'] == second_data['email']
    assert first_data['user']['bio'] == second_data['bio']


# testing put method

@pytest.mark.django_db
def test_put_unauthenticated():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'name',
        'email': 'mail@mail.com',
        'bio': 'bio',
        'password1': 'Testing123*',
        'password2': 'Testing123*'
    })
    assert response.status_code == 200

    response = client.put('/users/1/', {
        'username': 'another_name',
        'email': 'another_mail@mail.com',
        'bio': 'another bio'
    })

    assert response.status_code == 401


@pytest.mark.django_db
def test_put_authenticated_update_another_user(auth_client):
    user = {
        'username': 'gemmy',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'email': 'testing@testing.com',
        'bio': 'bio'
    }
    client = auth_client()
    response = client.post('/authentication/register/', user)
    user_id = response.data['user']['id']
    response = client.put(f'/users/{user_id}/', {
        'username': 'another_name',
        'email': 'another_mail@mail.com',
        'bio': 'another bio'
    })

    assert response.status_code == 403
