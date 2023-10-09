from locust import HttpUser, task, between

class AuthenticationUser(HttpUser):
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
    def authentication_internal(self):
        # Define the payload for the POST request
        payload = {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2OTE1NDM5LCJpYXQiOjE2ODQzMjM0MzksImp0aSI6Ijg4NTMxNjAzYmI1NzQ0Y2I5NDU3MjMwOWZmNWZlYTJhIiwidXNlcl9pZCI6ImZjOTRmZjc5LWVlOTgtNGRmOC1hNWFmLWRkOTE2YTUxOWI5MiJ9.RLH-20TY_MTVXgJ1JT_ShUHFF6fSwmF6C_eiLFOWatU"
        }

        # Send the POST request
        response = self.client.post("/v1/auth/public/authentication", json=payload, headers=self.headers)

        # Check the response
        if response.status_code == 200:
            print("Authentication successful")
        else:
            print("Authentication failed")

