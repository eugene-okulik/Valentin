import allure
import requests
from endpoints.endpoint import Endpoint


class GetAllData(Endpoint):

    @allure.step('Get all data')
    def get_all_data(self):
        self.response = requests.get(self.url)
