import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateDataPatch(Endpoint):

    @allure.step('Update name and/or data PATCH')
    def update_data_patch(self, body, prepared_json):
        url_with_id = f'{self.url}/{prepared_json['id']}'
        self.started_json = prepared_json
        self.response = requests.patch(url_with_id, json=body)
        self.json = self.response.json()
