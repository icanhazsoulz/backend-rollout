"""Unit test for application."""
import os
from app import app


def test_hello():

    """Returns Hello, KubeRocketCi!."""
    response = app.test_client().get('/api/hello')

    assert response.status_code == 200
    assert response.data == b'Hello, KubeRocketCI from ${os.getenv("HOSTNAME")}!'
