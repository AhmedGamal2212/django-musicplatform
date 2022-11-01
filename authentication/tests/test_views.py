import django.db.utils
import pytest
from rest_framework.test import APIClient


# testing register

@pytest.mark.django_db
def test_register_with_invalid_username():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy in testing',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_without_a_required_field():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': '',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_without_optional_field():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmyintesting',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': ''
    })
    user_data = response.data['user']
    assert response.status_code == 200
    assert user_data['username'] == 'gemmyintesting'
    assert user_data['email'] == 'gemmytesting@testing.com'
    assert user_data['bio'] == ''
    assert 'password' not in user_data and 'password1' not in user_data and 'password2' not in user_data
    assert 'token' in response.data


@pytest.mark.django_db
def test_register_with_passwords_dont_match():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_with_existing_username():
    client = APIClient()
    client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })

    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'anothermail@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })

    assert response.status_code == 400


@pytest.mark.django_db
def test_register_with_existing_email():
    client = APIClient()
    client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })
    response = client.post('/authentication/register/', {
        'username': 'another_username',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })
    assert response.status_code == 400

@pytest.mark.django_db
def test_register_with_weak_password():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Weak',
        'password2': 'Weak',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_with_entirely_missing_field():
    client = APIClient()
    with pytest.raises(django.db.utils.IntegrityError):
        response = client.post('/authentication/register/', {
            'username': 'gemmy',
            'email': 'gemmytesting@testing.com',
            'password1': 'Testing123*',
            'password2': 'Testing123*',
            # bio is missing
        })
        assert response.status_code == 500


@pytest.mark.django_db
def test_register_with_all_is_ok():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })
    user_data = response.data['user']
    assert response.status_code == 200
    assert user_data['username'] == 'gemmy'
    assert user_data['email'] == 'gemmytesting@testing.com'
    assert user_data['bio'] == 'anything'
    assert 'password' not in user_data and 'password1' not in user_data and 'password2' not in user_data
    assert 'token' in response.data


# testing login

@pytest.mark.django_db
def test_login_with_invalid_credentials():
    client = APIClient()
    response = client.post('/authentication/login/', {
        'username': 'gemmy',
        'password': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_with_all_is_ok():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'testing@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': 'anything'
    })
    token = response.data['token']
    token = 'Token ' + token
    client.credentials(HTTP_AUTHORIZATION=token)
    response = client.post('/authentication/login/', {
        'username': 'gemmy',
        'password': 'Testing123*'
    })
    user_data = response.data['user']
    assert response.status_code == 200
    assert user_data['username'] == 'gemmy'
    assert user_data['email'] == 'testing@testing.com'
    assert user_data['bio'] == 'anything'
    assert 'password' not in user_data
    assert 'token' in response.data


@pytest.mark.django_db
def testing_logout_with_already_logged_in_user():
    client = APIClient()
    token = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'testing@testing.com',
        'password1': 'Testing123*',
        'password2': 'Testing123*',
        'bio': ''
    }).data['token']
    token = 'Token ' + token
    client.credentials(HTTP_AUTHORIZATION=token)
    response = client.post('/authentication/logout/', {})
    assert response.status_code == 204


@pytest.mark.django_db
def test_logout_with_logged_out_user():
    client = APIClient()
    response = client.post('/authentication/logout/', {})
    assert response.status_code == 401
