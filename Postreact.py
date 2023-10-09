from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 to 5 seconds between requests

    @task
    def post_reaction(self):
        url = "https://staging.imlink.network/v1/reacts/private/like"

        payload = {
            "contentType": "post",
            "contentId": "8f947174-bc3e-4dd8-ab22-e44d41a9bd90",
            "reaction": "2110001"
        }

        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",  # Set Content-Length to 0
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.post(url, json=payload, headers=headers)

        # Check the response status code and apply an if condition
        if response.status_code == 200:
            self.locust.log_success("Post Reaction Successful", response.content)
        else:
            self.locust.log_failure("Post Reaction Failed", response.content)
