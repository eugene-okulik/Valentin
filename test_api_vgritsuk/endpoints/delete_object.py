import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.url = self.url + '/' + str(object_id)
        self.response = requests.delete(self.url)
