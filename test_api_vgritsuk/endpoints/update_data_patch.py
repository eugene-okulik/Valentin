from turtledemo.penrose import start

import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateDataPatch(Endpoint):

    @allure.step('Update name and/or data PATCH')
    def update_data_patch(self, body):
        self.url = self.url + '/' + str(self.json['id'])
        self.started_json = self.json
        self.response = requests.patch(self.url, json=body)
        self.json = self.response.json()
