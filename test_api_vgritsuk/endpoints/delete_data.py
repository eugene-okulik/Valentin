import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteData(Endpoint):

    @allure.step('Delete data')
    def delete_data(self, data_id):
        self.url = self.url + '/' + str(data_id)
        self.response = requests.delete(self.url)

    @allure.step('Check data is not exist')
    def check_deleted_data_is_really_deleted(self):
        self.response = requests.get(self.url)
        assert self.response.status_code == 404, f'Статус код = {self.response.status_code}'
