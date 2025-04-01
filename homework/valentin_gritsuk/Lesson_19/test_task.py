import requests
import pytest
import allure


@allure.feature('Left Feature')
@allure.story('Happy story')
@allure.title('Получаем всю инфу')
@pytest.mark.critical
def test_all_data(print_before_after_all_tests):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


@allure.feature('Left Feature')
@allure.story('Happy story')
@allure.title('Получаем одну инфу')
@pytest.mark.medium
def test_one_data(data_id):
    response = requests.get(f'http://167.172.172.115:52353/object/{data_id}').json()
    assert response['id'] == data_id, 'Id is incorrect'


@allure.feature('Left Feature')
@allure.story('Happy story')
@allure.title('Создаём новую инфу')
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


@allure.feature('Right Feature')
@allure.story('Sad story')
@allure.title('Меняем инфу с помощью пут')
def test_put_data(data_id):
    body = {
        "name": "fadas",
        "data": {"xcz": "weq", "fsdf": "aweq"}
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{data_id}',
        json=body,
    )
    with allure.step('Проверяем изменённый name'):
        assert response.json()['name'] == 'fadas', 'Name is incorrect'
    with allure.step('Проверяем изменённый data'):
        assert response.json()['data'] == {"xcz": "weq", "fsdf": "aweq"}, 'Data is incorrect'
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.feature('Right Feature')
@allure.story('Sad story')
@allure.title('Меняем инфу с помощью патч')
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


@allure.feature('Right Feature')
@allure.story('Sad story')
@allure.title('Удаляем инфу')
def test_delete_a_post(data_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{data_id}')
    assert response.status_code == 200
    assert requests.get(f'http://167.172.172.115:52353/object/{data_id}').status_code == 404
