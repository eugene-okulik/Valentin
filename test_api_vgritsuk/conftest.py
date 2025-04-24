import pytest
from endpoints.create_post import CreatePost
from endpoints.get_data import GetData
from endpoints.update_data_put import UpdateDataPut
from endpoints.update_data_patch import UpdateDataPatch
from endpoints.delete_data import DeleteData


DATA = {"name": "first", "data": {"color": "red", "size": "small"}}


@pytest.fixture()
def create_data_endpoint():
    return CreatePost()


@pytest.fixture()
def delete_data_endpoint():
    return DeleteData()


@pytest.fixture()
def get_data_endpoint():
    return GetData()


@pytest.fixture()
def update_data_put_endpoint():
    return UpdateDataPut()


@pytest.fixture()
def update_data_patch_endpoint():
    return UpdateDataPatch()


@pytest.fixture()
def prepared_data(create_data_endpoint, delete_data_endpoint):
    created_data = create_data_endpoint.create_new_data(DATA).json()
    yield created_data
    delete_data_endpoint.delete_data(created_data['id'])
