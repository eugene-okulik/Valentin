from locust import HttpUser, task, SequentialTaskSet


class UserBehavior(SequentialTaskSet):
    data = {"name": "first", "data": {"color": "red", "size": "small"}}
    data_upd = {"name": "second", "data": {"blue": "car", "size": "cat"}}
    object_id = None

    @task
    def create_new_object(self):
        response = self.client.post(
            '/object',
            json=self.data
        )
        self.object_id = response.json()['id']

    @task
    def get_one_object(self):
        self.client.get(
            f'/object/{self.object_id}'
        )

    @task
    def update_object_patch(self):
        self.client.patch(
            f'/object/{self.object_id}',
            json=self.data_upd
        )

    @task
    def update_object_put(self):
        self.client.put(
            f'/object/{self.object_id}',
            json=self.data
        )

    @task
    def delete_object(self):
        self.client.delete(
            f'/object/{self.object_id}'
        )


class ApiUser(HttpUser):
    tasks = [UserBehavior]  # Только последовательные задачи

    @task
    def get_all_objects(self):
        self.client.get('/object')