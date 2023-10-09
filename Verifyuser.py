from locust import HttpUser, task, between

class VerifyUser(HttpUser):
    host = "https://staging.imlink.network"  # Set the host URL
    wait_time = between(1, 5)  # Define the time range between requests

    def on_start(self):
        # Initialize the HTTP session with custom headers
        self.headers = {
            "Content-Type": "application/json",
            "Content-Length": "200",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

    @task(1)
    def verify_user(self):
        # Define the payload for the POST request
        payload = {
            "email": "Rewaa@link.com",
            "otp": "7456"
        }

        # Send the POST request
        response = self.client.post("/v1/auth/public/otp/verify", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("User verification successful")
        else:
            print("User verification failed")



