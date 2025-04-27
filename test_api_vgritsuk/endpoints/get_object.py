import allure
import requests
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)

    @allure.step('Get object by id')
    def get_data_by_id(self, object_id):
        url_with_id = f'{self.url}/{object_id}'
        self.response = requests.get(url_with_id)
        self.json = self.response.json()

    @allure.step('Check object is not exist')
    def check_object_is_missing(self, object_id):
        url_with_id = f'{self.url}/{object_id}'
        self.response = requests.get(url_with_id)
        assert self.response.status_code == 404, f'Статус код = {self.response.status_code}'
