import os
import pytest
from Movies import create_app
from Movies.adapters.memory_repository import MemoryRepository


TEST_DATA_PATH = os.path.join('Movies', 'tests', 'data')


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    # not sure what that does
    repo.populate("tests/data/Data1000Movies.csv", "tests/data/reviews.csv", "tests/data/users.csv")
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()


class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username='thorke', password='cLQ^C#oFXloS'):
        return self._client.post(
            '/login',
            data={'username': username, 'password': password})

    def logout(self):
        return self._client.post('/login', data={'button': 'logout'})


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)
