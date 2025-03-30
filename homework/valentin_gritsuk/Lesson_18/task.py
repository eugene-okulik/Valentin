import requests


def new_data():
    body = {
        "name": "testtest",
        "data" : {"color": "white", "size": "big"}
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
    )
    return response.json()['id']

def clear(post_id):
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')

def all_data():
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'

def one_data():
    post_id = new_data()
    response = requests.get(f'http://167.172.172.115:52353/object/{post_id}').json()
    assert response['id'] == post_id, 'Id is incorrect'
    clear(post_id)

def post_data():
    body = {
        "name": "testingtest",
        "data" : {"color": "white", "size": "big"}
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "testingtest", 'Name is incorrect'
    assert response.json()['data'] == {"color": "white", "size": "big"}, 'Data is incorrect'

def put_data():
    post_id = new_data()
    body = {
        "name": "fadas",
        "data" : {"xcz": "weq", "fsdf": "aweq"}
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
    )
    assert response.json()['name'] == 'fadas', 'Name is incorrect'
    assert response.json()['data'] == {"xcz": "weq", "fsdf": "aweq"}, 'Data is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'
    clear(post_id)


def patch_data():
    post_id = new_data()
    body = {
        "name": "fadas",
        "data": {"xcz": "weq", "fsdf": "aweq"}
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
    )
    assert response.json()['name'] == 'fadas', 'Name is incorrect'
    assert response.json()['data'] == {"xcz": "weq", "fsdf": "aweq"}, 'Data is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'
    clear(post_id)


def delete_a_post():
    post_id = new_data()
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200
    assert requests.get(f'http://167.172.172.115:52353/object/{post_id}').status_code == 404


all_data()
one_data()
post_data()
put_data()
patch_data()
delete_a_post()
