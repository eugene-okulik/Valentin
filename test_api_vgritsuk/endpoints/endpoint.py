import requests
import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    started_json = None
    json = None

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check that data in json is the same as sent')
    def check_response_data_is_correct(self, data):
        assert self.json['data'] == data

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400
