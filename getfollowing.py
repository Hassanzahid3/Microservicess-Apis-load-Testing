from locust import HttpUser, task, between

class GetFollowing(HttpUser):

    host = "https://staging.imlink.network"
    endpoint = "/v1/users/private/following?page-number=1&items-per-page=5"
    wait_time = between(1, 3)

    @task
    def get_following(self):
        response = self.client.get(f"{self.host}{self.endpoint}")

        # You can check the response if needed
        if response.status_code == 200:
            # Successful response handling here
            pass
        else:
            # Handle other responses here
            pass
