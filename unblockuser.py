from locust import HttpUser, task, between

class UnblockUser(HttpUser):

    host = "https://staging.imlink.network"
    endpoint = "/v1/users/private/unblock"
    wait_time = between(1, 3)

    @task
    def unblock_user(self):
        payload = {
            "userId": "32321b04-ff15-4143-8309-d1d901c965c4"
        }

        headers = {"Content-Type": "application/json"}
        response = self.client.post(
            f"{self.host}{self.endpoint}",
            json=payload,
            headers=headers
        )

        # You can check the response if needed
        if response.status_code == 200:
            # Successful response handling here
            pass
        else:
            # Handle other responses here
            pass
