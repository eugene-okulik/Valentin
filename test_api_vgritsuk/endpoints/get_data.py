import allure
import requests
from endpoints.endpoint import Endpoint


class GetData(Endpoint):

    @allure.step('Get all data')
    def get_all_data(self):
        self.response = requests.get(self.url)

    @allure.step('Get data by id')
    def get_data_by_id(self, data_id):
        url_with_id = f'{self.url}/{data_id}'
        self.response = requests.get(url_with_id)
        self.json = self.response.json()
