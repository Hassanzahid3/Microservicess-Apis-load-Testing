#get followings id internal
from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def get_following_ids(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*"
        }

        response = self.client.get(
            "/v1/users/private/following-ids",
            headers=headers
        )

        if response.status_code == 200:
            pass
        else:
            pass