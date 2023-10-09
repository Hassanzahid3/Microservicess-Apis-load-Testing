from locust import HttpUser, task, between

class GetSinglePostUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def get_single_post(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        # Replace {post_id} with the actual post ID you want to retrieve
        post_id = "5e337fae-26e6-49d5-b6b2-255f7f795f43"

        response = self.client.get(
            f"/v1/posts/private/post-detail/{post_id}",
            headers=headers
        )

        if response.status_code == 200:
            pass  # Handle a successful response if needed
        else:
            pass  # Handle an unsuccessful response if needed


