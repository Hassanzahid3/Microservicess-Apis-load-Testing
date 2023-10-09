from locust import HttpUser, task, between

class LoginUser(HttpUser):
    host = "https://staging.imlink.network"  # Set the host URL
    wait_time = between(1, 5)  # Define the time range between requests

    def on_start(self):
        # Initialize the HTTP session with custom headers
        self.headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Accept": "application/json"
        }

    @task(1)
    def login(self):
        # Define the payload for the POST request
        payload = {
            "usernameOrEmail": "ram.2277@outlook.com",
            "password": "Rewaa12345",
            "deviceType": "IOS",
            "osVersion": "30.1",
            "deviceId": "123456"
        }

        # Send the POST request
        response = self.client.post("/v1/auth/public/login", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("Login successful")
        else:
            print("Login failed")


