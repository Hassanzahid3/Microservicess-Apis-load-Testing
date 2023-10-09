from locust import HttpUser, task, between

class ResendOTPUser(HttpUser):
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
    def resend_otp(self):
        # Define the payload for the PUT request
        payload = {
            "email": "hassanrajpoot6330@gmail.com"
        }

        # Send the PUT request
        response = self.client.put("/v1/auth/public/otp/resend", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("OTP resend successful")
        else:
            print("OTP resend failed")

