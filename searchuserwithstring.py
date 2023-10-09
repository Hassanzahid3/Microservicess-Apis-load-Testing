from locust import HttpUser, task, between

class Searchuserwithstring(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def Searchuserwithstring(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(
            "/v1/users/private/search-user?search=a&page-number=1&items-per-page=50",
            headers=headers
        )

        if response.status_code == 200:
            # You can add your verification or validation logic here
            pass
        else:
            # Handle the response when it's not 200 (e.g., logging or reporting)
            pass
