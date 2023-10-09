from locust import HttpUser, task, between


class AcceptFollowRequestUser(HttpUser):
    host     = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def accept_follow_request(self):
        # Define the JSON payload for accepting a follow request
        payload = {
            "followRequestId": "cb136675-36d6-44e1-a613-f2566dc6bf1d"
        }

        headers = {"Content-Type": "application/json"}

        response = self.client.post(
            "/v1/users/private/accept-follow-request",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            # Request was successful
            pass
        else:
            # Handle other responses here
            pass
