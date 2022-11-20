from rest_framework import status
import pytest
from model_bakery import baker

from blog.models import Post


@pytest.mark.django_db
class TestListofPost:
    def test_list_post(self, api_client):
        post = baker.make(Post)
        response = api_client()

        assert response.status_code == status.HTTP_200_OK