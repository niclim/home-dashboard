import json


def test_example(client):
    response = client.get("/example")

    assert response.status_code == 200
    assert json.loads(response.data.decode("utf-8"))["data"] == "hello"
