import pytest

DATA = {"name": "first", "data": {"color": "red", "size": "small"}}
FULL_DATA_UPDATE = {"name": "first", "data": {"color": "red", "size": "small"}}
DATA_UPDATE_NAME = {"name": "update"}
DATA_UPDATE_DATA = {"data": {"update": "redd", "ssize": "small"}}
PARAM_DATA = [{"name": "first", "data": {"color": "red", "size": "small"}},
              {"name": "second", "data": {"color": "green", "size": "medium"}},
              {"name": "third", "data": {"color": "blue", "size": "large"}}]


def test_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_that_status_is_200()


def test_get_object_by_id(get_object_endpoint, prepared_object):
    get_object_endpoint.get_data_by_id(prepared_object['id'])
    get_object_endpoint.check_that_status_is_200()
    get_object_endpoint.check_response_name_is_correct(DATA['name'])
    get_object_endpoint.check_response_data_is_correct(DATA['data'])


@pytest.mark.parametrize("test_object", PARAM_DATA)
def test_post_data(test_object, create_object_endpoint, delete_object_endpoint):
    create_object_endpoint.create_new_object(test_object)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(test_object['name'])
    create_object_endpoint.check_response_data_is_correct(test_object['data'])
    delete_object_endpoint.delete_object(create_object_endpoint.json['id'])


def test_put_data(update_object_put_endpoint, prepared_object):
    update_object_put_endpoint.update_object_put(FULL_DATA_UPDATE, prepared_object['id'])
    update_object_put_endpoint.check_response_name_is_correct(FULL_DATA_UPDATE['name'])
    update_object_put_endpoint.check_response_data_is_correct(FULL_DATA_UPDATE['data'])


def test_patch_data(update_object_patch_endpoint, prepared_object):
    update_object_patch_endpoint.update_object_patch(DATA_UPDATE_NAME, prepared_object)
    update_object_patch_endpoint.check_response_name_is_correct(DATA_UPDATE_NAME['name'])
    update_object_patch_endpoint.check_response_data_is_correct(update_object_patch_endpoint.started_json['data'])


def test_delete_data(delete_object_endpoint, prepared_object, get_object_endpoint):
    delete_object_endpoint.delete_object(prepared_object['id'])
    get_object_endpoint.check_object_is_missing(prepared_object['id'])
