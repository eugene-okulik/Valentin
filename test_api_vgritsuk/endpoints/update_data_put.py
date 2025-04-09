import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateDataPut(Endpoint):


    @allure.step('Update name and/or data')
    def update_data_put(self, body):
        self.url = self.url + '/' + str(self.json['id'])
        self.response = requests.put(self.url, json=body)


    @allure.step('Check response-json and started-json are same')
    def check_name_and_data_are_correct(self, body):
        assert self.json['name'] == body['name']
        assert self.json['data'] == body['data']