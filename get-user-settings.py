from locust import HttpUser, task, between


class GetUserSettingsUser(HttpUser):
    host = "https://staging.imlink.network"  # Update the host URL as needed
    wait_time = between(1, 3)  # Adjust the wait time as needed

    @task
    def get_user_settings(self):
        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send a GET request to the /v1/users/private/settings endpoint
        response = self.client.get("/v1/users/private/settings", headers=headers)

        # Check the response status code
        if response.status_code == 200:
            # If the response is successful (status code 200), you can add your verification logic here
            pass
        else:
            # Handle the response when it's not 200 (e.g., logging or reporting)
            pass



