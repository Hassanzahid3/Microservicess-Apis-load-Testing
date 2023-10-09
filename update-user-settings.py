from locust import HttpUser, task, between


class UpdateUserSettingsUser(HttpUser):
    host = "https://staging.imlink.network"  # Update the host URL as needed
    wait_time = between(1, 3)  # Adjust the wait time as needed

    @task
    def update_user_settings(self):
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Define the payload
        payload = {
            "profileType": "private",
            "nearby": True,
            "pushNotification": False,
            "anonymousChat": True,
            "dmNotification": True,
            "emailNotification": True
        }

        # Send a PUT request to the /v1/users/private/settings endpoint with the payload
        response = self.client.put("/v1/users/private/settings", json=payload, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            # If the response is successful (status code 200), you can add your verification logic here
            pass
        else:
            # Handle the response when it's not 200 (e.g., logging or reporting)
            pass


if __name__ == "__main__":
    import os

    os.system("locust -f locust_file.py")  # Replace "locust_file.py" with the name of your Locust script
