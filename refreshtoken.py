from locust import HttpUser, task, between

class RefreshTokenUser(HttpUser):
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
    def refresh_token(self):
        # Define the payload for the POST request
        payload = {
            "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwOTc3MjMyLCJpYXQiOjE2ODgzODUyMzIsImp0aSI6ImI3NGFiODc0YWZmOTQwZTNhNmVkYWE3NGUwNmJhYTZlIiwidXNlcl9pZCI6IjNmZmI5N2I5LTNhNDMtNDlhNC05ZjlhLTVhY2ZmZWZjNjZiMyJ9.YcImMA3CAA0YOBspXnTAMdms6ddVUYdhYbLuHWtio8c"
        }

        # Send the POST request
        response = self.client.post("/v1/auth/public/refresh", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("Token refresh successful")
        else:
            print("Token refresh failed")


