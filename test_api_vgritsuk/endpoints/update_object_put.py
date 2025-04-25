import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateObjectPut(Endpoint):

    @allure.step('Update name and/or data')
    def update_object_put(self, body, data_id):
        url_with_id = f'{self.url}/{data_id}'
        self.response = requests.put(url_with_id, json=body)
        self.json = self.response.json()
