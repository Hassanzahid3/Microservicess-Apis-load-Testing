from locust import HttpUser, task, between


class CreateUserPostsUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def create_post(self):
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "20",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        payload = {
            "postType": "text",
            "postContent": "my post for testing - abdo hahaha"
        }

        response = self.client.post(
            "/v1/posts/private/user-posts",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            pass  # Handle a successful response if needed
        else:
            pass  # Handle an unsuccessful response if needed
