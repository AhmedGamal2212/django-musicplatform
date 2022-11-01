import pytest
from rest_framework.test import APIClient
from users.models import CustomUser
from knox.auth import AuthToken

testing_user = {
    'username': 'testing user',
    'email': 'testinguser@testing.com',
    'password': 'testing123'
}


@pytest.fixture
def auth_client():
    def get_client(user=None):
        client = APIClient()
        if user is None:
            user = CustomUser.objects.create_user(
                username=testing_user['username'],
                email=testing_user['email'],
                password=testing_user['password'],
            )

        _, token = AuthToken.objects.create(user)
        token = 'Token ' + token
        client.credentials(HTTP_AUTHORIZATION=token)

        return client

    return get_client
