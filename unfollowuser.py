from locust import HttpUser, task, between

class UnfollowUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def unfollow(self):
        payload = {
            "userId": "4a8185bd-a0c3-426f-99df-233f5af19557"
        }

        headers = {"Content-Type": "application/json"}

        response = self.client.delete(
            "/v1/users/private/unfollow",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            pass
        else:
            # Handle other responses here
            pass
