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
