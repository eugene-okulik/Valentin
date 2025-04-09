import pytest

DATA = {"name": "first", "data": {"color": "red", "size": "small"}}
FULL_DATA_UPDATE = {"name": "first", "data": {"color": "red", "size": "small"}}
DATA_UPDATE_NAME = {"name": "update"}
DATA_UPDATE_DATA = {"data": {"update": "redd", "ssize": "small"}}
PARAM_DATA = [{"name": "first", "data": {"color": "red", "size": "small"}},
              {"name": "second", "data": {"color": "green", "size": "medium"}},
              {"name": "third", "data": {"color": "blue", "size": "large"}}]


def test_get_all_data(get_all_data_endpoint):
    get_all_data_endpoint.get_all_data()
    get_all_data_endpoint.check_that_status_is_200()


def test_get_data_by_id(get_data_by_id_endpoint, prepared_data_get_data_by_id_endpoint):
    get_data_by_id_endpoint.get_data_by_id()
    get_data_by_id_endpoint.check_that_status_is_200()
    get_data_by_id_endpoint.check_response_name_is_correct(DATA['name'])
    get_data_by_id_endpoint.check_response_data_is_correct(DATA['data'])


@pytest.mark.parametrize("test_data", PARAM_DATA)
def test_post_data(test_data, create_data_endpoint):
    create_data_endpoint.create_new_data(test_data)
    create_data_endpoint.check_that_status_is_200()
    create_data_endpoint.check_response_name_is_correct(test_data['name'])
    create_data_endpoint.check_response_data_is_correct(test_data['data'])
    create_data_endpoint.delete_new_data()


def test_put_data(update_data_put_endpoint, prepared_data_update_data_put_endpoint):
    update_data_put_endpoint.update_data_put(FULL_DATA_UPDATE)
    update_data_put_endpoint.check_name_and_data_are_correct(FULL_DATA_UPDATE)


def test_patch_data(update_data_patch_endpoint, prepared_data_update_data_patch_endpoint):
    update_data_patch_endpoint.update_data_patch(DATA_UPDATE_NAME)
    update_data_patch_endpoint.check_response_name_is_correct(DATA_UPDATE_NAME['name'])
    update_data_patch_endpoint.check_response_data_is_correct(update_data_patch_endpoint.started_json['data'])


def test_delete_data(delete_data_endpoint, prepared_delete_data_endpoint):
    delete_data_endpoint.delete_data()
    delete_data_endpoint.check_deleted_data_is_really_deleted()
