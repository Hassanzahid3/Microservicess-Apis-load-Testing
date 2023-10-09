from locust import HttpUser, task, between

class VerifyUpdateEmailUser(HttpUser):
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

    @task
    def verify_update_email(self):
        # Define the payload for the POST request
        payload = {
            "email": "some@gmail.com",
            "otp": "2647"
        }

        # Send the POST request
        response = self.client.post("/v1/auth/private/otp/email-update", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("Email verification and update successful")
        else:
            print("Email verification and update failed")


