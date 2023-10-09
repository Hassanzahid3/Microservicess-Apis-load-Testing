from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def get_follow_requests(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(
            "/v1/users/private/follow-requests?page-number=1&items-per-page=5",
            headers=headers
        )

        if response.status_code == 200:
            pass
        else:
            pass
