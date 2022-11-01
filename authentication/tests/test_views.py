import django.db.utils
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_with_invalid_username():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy in testing',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_without_a_required_field():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': '',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_without_optional_field():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmyintesting',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': ''
    })
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_with_passwords_dont_match():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212',
        'bio': 'anything'
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_with_existing_username():
    client = APIClient()
    client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': 'anything'
    })

    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'anothermail@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': 'anything'
    })

    assert response.status_code == 400


@pytest.mark.django_db
def test_register_with_existing_email():
    client = APIClient()
    client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': 'anything'
    })
    response = client.post('/authentication/register/', {
        'username': 'another_username',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
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
            'password1': 'Ahmed2212@',
            'password2': 'Ahmed2212@',
            # bio is missing
        })
        assert response.status_code == 500


@pytest.mark.django_db
def test_register_with_all_is_ok():
    client = APIClient()
    response = client.post('/authentication/register/', {
        'username': 'gemmy',
        'email': 'gemmytesting@testing.com',
        'password1': 'Ahmed2212@',
        'password2': 'Ahmed2212@',
        'bio': 'anything'
    })
    assert response.status_code == 200
