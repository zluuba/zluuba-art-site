from pytest import fixture
from zluuba_art.app import app


@fixture
def test_app():
    app.config.update({
        "TESTING": True,
    })

    yield app


@fixture
def client(test_app):
    return test_app.test_client()
