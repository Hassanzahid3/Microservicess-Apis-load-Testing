from locust import HttpUser, task, between

class UpdateComment(HttpUser):

    host = "https://staging.imlink.network"
    endpoint = "/v1/comments/private/comment/7484d235-0493-4e70-8e58-855702185f92"
    wait_time = between(1, 3)

    @task
    def update_comment(self):
        payload = {
            "comment": "good job v good",
            "commentType": "gif"
        }

        headers = {"Content-Type": "application/json"}
        response = self.client.put(
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
