import pytest
from rest_framework.test import APIClient

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
