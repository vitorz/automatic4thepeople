import pytest
import http.client


def test_the_sample_app_is_up():
    connection = http.client.HTTPConnection("localhost:8080")
    connection.request("GET", "/sample/")
    response = connection.getresponse()
    connection.close()
    assert response.status == 200