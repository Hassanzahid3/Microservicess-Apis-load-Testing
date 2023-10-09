from locust import HttpUser, task, between

class ForgetPasswordUser(HttpUser):
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
            "Host": "staging.imlink.network",
        }

    @task(1)
    def forget_password(self):
        # Define the payload for the PUT request
        payload = {
            "email": "hassanrajpoot6330@gmail.com"
        }

        # Send the PUT request
        response = self.client.put("/v1/auth/public/forget-password", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("Password reset initiated successfully")
        else:
            print("Password reset initiation failed")


