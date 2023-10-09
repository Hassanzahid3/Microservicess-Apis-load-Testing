from locust import HttpUser, task, between

class GetFollowers(HttpUser):

    host = "https://staging.imlink.network"
    endpoint = "/v1/users/private/follower?page-number=1&items-per-page=20"   # param are define in this url
    wait_time = between(1, 3)

    @task
    def get_followers(self):
        response = self.client.get(f"{self.host}{self.endpoint}")

        # response
        if response.status_code == 200:
            # Successful response handling here
            pass
        else:
            # Handle other responses here
            pass
