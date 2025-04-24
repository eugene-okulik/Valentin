import allure
from endpoints.endpoint import Endpoint
import requests


class CreatePost(Endpoint):

    @allure.step('Create new data')
    def create_new_data(self, body):
        self.response = requests.post(
            self.url,
            json=body
        )
        self.json = self.response.json()
        return self.response
