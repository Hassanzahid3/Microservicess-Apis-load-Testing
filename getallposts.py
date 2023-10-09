from locust import HttpUser, task, between

class GetAllPostsUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def get_all_posts(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        response = self.client.get(
            "/v1/posts/private/user-posts?page-number=1&items-per-page=20",
            headers=headers
        )

        if response.status_code == 200:
            pass  # Handle a successful response if needed
        else:
            pass  # Handle an unsuccessful response if needed

