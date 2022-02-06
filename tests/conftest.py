import pytest
from app import create_app
from config import Config

from app.extensions import db

@pytest.fixture
def testing_client():
    app = create_app(Config, testing=True)

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture()
def urls():
    urls = ['/v1/api/wojewodztwa', '/v1/api/powiaty', '/v1/api/gminy', '/v1/api/stats']

    return urls


@pytest.fixture
def transaction():
    with db.transaction() as txn:  # `db` is my database object
        yield txn
        txn.rollback()
