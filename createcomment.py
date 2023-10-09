from locust import HttpUser, task, between

class CreateComment(HttpUser):

    host = "https://staging.imlink.network"
    endpoint = "/vi/comments/private/comment"
    wait_time = between(1, 3)

    @task
    def create_comment(self):
        payload = {
            "contentId": "8f947174-bc3e-4dd8-ab22-e44d41a9bd90",
            "comment": "dont rush now",
            "contentType": "post"
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
