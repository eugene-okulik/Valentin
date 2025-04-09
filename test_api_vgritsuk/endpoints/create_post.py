import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400
    # Если получилось, что в Create Post нечего вписывать, нужен ли этот класс для этого эндпоинта ?
