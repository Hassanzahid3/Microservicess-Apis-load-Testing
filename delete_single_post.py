from locust import HttpUser, task, between

class DeleteSinglePostUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def delete_single_post(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        # Replace {post_id} with the actual post ID you want to delete
        post_id = "0a05c76a-d7b5-4ac0-96ec-2323ea4d2572"

        response = self.client.delete(
            f"/v1/posts/private/post-detail/{post_id}",
            headers=headers
        )

        if response.status_code == 204:
            pass  # Handle a successful deletion (status code 204) if needed
        else:
            pass  # Handle an unsuccessful response if needed
