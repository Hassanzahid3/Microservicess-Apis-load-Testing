from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://staging.imlink.network"

    wait_time = between(1, 5)  # Set the wait time between requests

    @task
    def enabledisablenearbydevice(self):
        # Define the URL
        url = f"{self.host}/v1/users/private/switch-nearby"

        # Define the payload
        payload = {
            "nearby": False
        }

        # Define headers
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send the PUT request
        response = self.client.put(url, json=payload, headers=headers)

        # Check the response status code and content
        if response.status_code == 200:
            # Request was successful
            self.environment.events.request_success.fire(
                request_type="PUT",
                name="Update User Nearby",
                response_time=response.elapsed.total_seconds(),
                response_length=len(response.content),
                response=response,
            )
        else:
            # Request failed
            self.environment.events.request_failure.fire(
                request_type="PUT",
                name="Update User Nearby",
                response_time=response.elapsed.total_seconds(),
                response_length=len(response.content),
                exception=None,
            )
