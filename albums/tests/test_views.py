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



# @pytest.mark.django_db
# def test_manual_filtered_list_request_unauthenticated():
#     client = APIClient()
#     response = client.get('/albums/manual/')
#
#     assert response.status_code == 200
#     data = response.data
#     assert 'count' in data
#     assert data['count'] == math.ceil()
