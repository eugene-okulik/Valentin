import pytest
from endpoints.create_post import CreatePost
from endpoints.get_all_data import GetAllData
from endpoints.get_data_by_id import GetDataById
from endpoints.update_data_put import UpdateDataPut
from endpoints.update_data_patch import UpdateDataPatch
from endpoints.delete_data import DeleteData


DATA = {"name": "first", "data": {"color": "red", "size": "small"}}

@pytest.fixture()
def create_data_endpoint():
    return CreatePost()

@pytest.fixture()
def prepared_create_data_endpoint(create_data_endpoint):
    create_data_endpoint.create_new_data(DATA)
    yield
    create_data_endpoint.delete_new_data()


@pytest.fixture()
def get_all_data_endpoint():
    return GetAllData()


@pytest.fixture()
def get_data_by_id_endpoint():
    return GetDataById()



@pytest.fixture()
def prepared_data_get_data_by_id_endpoint(get_data_by_id_endpoint):
    get_data_by_id_endpoint.create_new_data(DATA)
    yield
    get_data_by_id_endpoint.delete_new_data()


@pytest.fixture()
def update_data_put_endpoint():
    return UpdateDataPut()


@pytest.fixture()
def prepared_data_update_data_put_endpoint(update_data_put_endpoint):
    update_data_put_endpoint.create_new_data(DATA)
    yield
    update_data_put_endpoint.delete_new_data()



@pytest.fixture()
def update_data_patch_endpoint():
    return UpdateDataPatch()




@pytest.fixture()
def prepared_data_update_data_patch_endpoint(update_data_patch_endpoint):
    update_data_patch_endpoint.create_new_data(DATA)
    yield
    update_data_patch_endpoint.delete_new_data()

@pytest.fixture()
def delete_data_endpoint():
    return DeleteData()

@pytest.fixture()
def prepared_delete_data_endpoint(delete_data_endpoint):
    delete_data_endpoint.create_new_data(DATA)


# @pytest.fixture()
# def create_delete_data_for_test(get_data_by_id_endpoint):
#     payload = {"title": "My generic tile", "body": "my body", "userId": 1}
#     get_data_by_id_endpoint.create_new_data(payload)
#     yield get_data_by_id_endpoint.delete_new_data()


