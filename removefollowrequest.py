from locust import HttpUser, task, between


class RemoveFollowRequest(HttpUser):
    host = "https://staging.imlink.network"
    endpoint = "/v1/users/private/remove-follow-request"
    wait_time = between(1, 3)

    @task
    def remove_follow_request(self):
        follow_request_id = "9b484be0-2257-43c3-8ff2-aa942806d29e"

        headers = {"Content-Type": "application/json"}
        response = self.client.delete(
            f"{self.endpoint}/{follow_request_id}",
            headers=headers
        )

        # conditions
        if response.status_code == 204:
            # Successful response handling here (assuming 204 No Content for successful delete)
            pass
        else:
            # Handle other responses here
            pass
