import requests
import pytest


@pytest.fixture(scope="session")
def print_before_after_all_tests():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def print_before_after_each_test():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def data_id():
    body = {
        "name": "testtest",
        "data": {"color": "white", "size": "big"}
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
    )
    yield response.json()['id']
    requests.delete(f"http://167.172.172.115:52353/object/{response.json()['id']}")
