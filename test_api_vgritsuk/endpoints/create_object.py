import allure
from endpoints.endpoint import Endpoint
import requests


class CreateObject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, body):
        self.response = requests.post(
            self.url,
            json=body
        )
        self.json = self.response.json()
        return self.response
