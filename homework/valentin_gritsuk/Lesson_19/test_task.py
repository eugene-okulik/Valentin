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


@pytest.mark.critical
def test_all_data(print_before_after_all_tests):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.medium
def test_one_data(data_id):
    response = requests.get(f'http://167.172.172.115:52353/object/{data_id}').json()
    assert response['id'] == data_id, 'Id is incorrect'


@pytest.mark.parametrize("test_data", [
    {
        "name": "first",
        "data": {"color": "red", "size": "small"}
    },
    {
        "name": "second",
        "data": {"color": "green", "size": "medium"}
    },
    {
        "name": "third",
        "data": {"color": "blue", "size": "large"}
    }
])
def test_post_data(test_data):
    body = test_data
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == test_data['name'], 'Name is incorrect'
    assert response.json()['data'] == test_data['data'], 'Data is incorrect'
    requests.delete(f"http://167.172.172.115:52353/object/{response.json()['id']}")


def test_put_data(data_id):
    body = {
        "name": "fadas",
        "data": {"xcz": "weq", "fsdf": "aweq"}
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{data_id}',
        json=body,
    )
    assert response.json()['name'] == 'fadas', 'Name is incorrect'
    assert response.json()['data'] == {"xcz": "weq", "fsdf": "aweq"}, 'Data is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'


def test_patch_data(data_id):
    body = {
        "name": "fadas",
        "data": {"xcz": "weq", "fsdf": "aweq"}
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{data_id}',
        json=body,
    )
    assert response.json()['name'] == 'fadas', 'Name is incorrect'
    assert response.json()['data'] == {"xcz": "weq", "fsdf": "aweq"}, 'Data is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'


def test_delete_a_post(data_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{data_id}')
    assert response.status_code == 200
    assert requests.get(f'http://167.172.172.115:52353/object/{data_id}').status_code == 404
