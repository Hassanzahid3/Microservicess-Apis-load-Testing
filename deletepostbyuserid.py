from locust import HttpUser, task, between

class GetPostByUserIDUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def get_post_by_user_id(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        user_id = "4a8185bd-a0c3-426f-99df-233f5af19557"  # Replace with the actual user ID

        response = self.client.get(
            f"/v1/posts/private/user-posts/{user_id}?page-number=1&items-per-page=10",
            headers=headers
        )

        if response.status_code == 200:
            pass  # Handle a successful response (status code 200) if needed
        else:
            pass  # Handle an unsuccessful response if needed

