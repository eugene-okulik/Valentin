import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


DATA = {"name": "first", "data": {"color": "red", "size": "small"}}


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def update_object_put_endpoint():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_patch_endpoint():
    return UpdateObjectPatch()


@pytest.fixture()
def prepared_object(create_object_endpoint, delete_object_endpoint):
    created_object = create_object_endpoint.create_new_object(DATA).json()
    yield created_object
    delete_object_endpoint.delete_object(created_object['id'])
