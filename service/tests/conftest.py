import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def logged_in_user(client):
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="password")
    client.login(username="testuser", password="password")
    return user
