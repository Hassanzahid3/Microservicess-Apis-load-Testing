from locust import HttpUser, task, between


class FollowUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def follow(self):
        payload = {
            "userId": "079c81d5-2705-4c99-8683-03dbed0b83ff"
        }

        # Send a POST request to follow user
        headers = {"Content-Type": "application/json"}
        response = self.client.post(
            "/v1/users/private/follow",
            json=payload,
            headers=headers
        )


        if response.status_code == 200:
            # Successful response handling here
            pass
        else:
            # Handle other responses here
            pass