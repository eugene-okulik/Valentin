import allure
import requests

from endpoints.endpoint import Endpoint


class GetDataById(Endpoint):


    @allure.step('Get data by id')
    def get_data_by_id(self):
        self.url = self.url + '/' + str(self.json['id'])
        self.response = requests.get(self.url)


