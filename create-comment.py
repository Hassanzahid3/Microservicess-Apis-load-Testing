from locust import HttpUser, task, between

class CreateCommentUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def create_comment(self):
        endpoint = "/v1/comments/private/comment"

        headers = {
            "Content-Type": "application/json",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "contentId": "8f947174-bc3e-4dd8-ab22-e44d41a9bd90",
            "comment": "dont rush now",
            "contentType": "post"
        }

        response = self.client.post(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Create Comment Successful")
        else:
            self.log.error("Create Comment Failed")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")  # Replace with the name of your Locust file
