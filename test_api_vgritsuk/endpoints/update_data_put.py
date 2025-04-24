import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateDataPut(Endpoint):

    @allure.step('Update name and/or data')
    def update_data_put(self, body, data_id):
        url_with_id = f'{self.url}/{data_id}'
        self.response = requests.put(url_with_id, json=body)
        self.json = self.response.json()

    @allure.step('Check response-json and started-json are same')
    def check_name_and_data_are_correct(self, body):
        assert self.json['name'] == body['name']
        assert self.json['data'] == body['data']
