import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteData(Endpoint):

    @allure.step('Delete data')
    def delete_data(self):
        self.url = self.url + '/' + str(self.json['id'])
        self.response = requests.delete(self.url)


    @allure.step('Check that deleted data is really deleted')
    def check_deleted_data_is_really_deleted(self):
        self.response = requests.get(self.url)
        assert self.response.status_code == 404, f'Статус код = {self.response.status_code}'

