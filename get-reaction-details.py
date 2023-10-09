from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 to 5 seconds between requests

    host = "https://staging.imlink.network"  # Define the host here

    @task
    def get_reaction_detail(self):
        endpoint = "/v1/reacts/private/likes-detail?contentId=ce1ac61a-c2e0-4ff8-82fe-2a35973b0d41"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        # Check the response status code and apply an if-else condition
        if response.status_code == 200:
            self.locust.log_success("Get Reaction Detail Successful", response.content)
        else:
            self.locust.log_failure("Get Reaction Detail Failed", response.content)
