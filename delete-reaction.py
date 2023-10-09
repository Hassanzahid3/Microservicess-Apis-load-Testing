from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 to 5 seconds between requests

    host = "https://staging.imlink.network"  # Define the host here

    @task
    def delete_reaction(self):
        endpoint = "/v1/reacts/private/like"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "contentId": "ce1ac61a-c2e0-4ff8-82fe-2a35973b0d41"
        }

        response = self.client.delete(endpoint, json=payload, headers=headers)

        # Check the response status code and apply an if-else condition
        if response.status_code == 204:  # Assuming 204 indicates successful deletion
            self.locust.log_success("Delete Reaction Successful", response.content)
        else:
            self.locust.log_failure("Delete Reaction Failed", response.content)
