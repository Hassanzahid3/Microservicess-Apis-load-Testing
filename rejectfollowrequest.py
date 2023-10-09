from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Specify a wait time range between requests

    @task
    def reject_follow_request(self):
        # Define the base URL and endpoint
        base_url = "https://staging.imlink.network"
        endpoint = "/v1/user/reject-follow-request"

        # Define headers
        headers = {
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
        }

        # Define the JSON payload
        payload = {
            "followRequestId": "9b484be0-2257-43c3-8ff2-aa942806d29e"
        }

        # Send the PUT request
        response = self.client.put(f"{base_url}{endpoint}", json=payload, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            self.environment.events.request_success.fire(
                request_type="PUT",
                name=endpoint,
                response_time=response.elapsed.total_seconds(),
                response_length=len(response.content),
            )
        else:
            self.environment.events.request_failure.fire(
                request_type="PUT",
                name=endpoint,
                response_time=response.elapsed.total_seconds(),
                exception=None,  # You can specify an exception here if needed
            )
