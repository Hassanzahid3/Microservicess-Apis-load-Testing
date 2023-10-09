from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://staging.imlink.network"

    wait_time = between(1, 5)  # Set the wait time between requests

    @task
    def get_nearby_user_range(self):
        # Define the endpoint URL
        endpoint = "/v1/nearby/private/nearby-range?min-latitude=28.611962&max-latitude=35.914025&min-longitude=68.047595&max-longitude=75.413915"
        url = f"{self.host}{endpoint}"

        # Define headers
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send the GET request
        response = self.client.get(url, headers=headers)

        # Check the response status code and content
        if response.status_code == 200:
            # Request was successful
            self.environment.events.request_success.fire(
                request_type="GET",
                name="Get Nearby User Range",
                response_time=response.elapsed.total_seconds(),
                response_length=len(response.content),
                response=response,
            )
        else:
            # Request failed
            self.environment.events.request_failure.fire(
                request_type="GET",
                name="Get Nearby User Range",
                response_time=response.elapsed.total_seconds(),
                response_length=len(response.content),
                exception=None,
            )
