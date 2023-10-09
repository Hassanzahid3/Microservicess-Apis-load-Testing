from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://staging.imlink.network"

    wait_time = between(1, 5)  # Set the wait time between requests

    @task
    def updateuserlocation(self):
        # Define the endpoint and payload
        endpoint = "/v1/nearby/private/nearby-range?min-latitude=28.611962&max-latitude=35.914025&min-longitude=68.047595&max-longitude=75.413915"
        url = f"{self.host}{endpoint}"  # Corrected reference to self.host
        payload = {
            "latitude": 31.7091758473,
            "longitude": 73.9848945803
        }

        # Define headers
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send the POST request
        response = self.client.post(url, json=payload, headers=headers)  # Use json parameter to send JSON payload

        # Check the response status code and content
        if response.status_code == 200:
            # You can add additional assertions or log the response content here
            pass
        else:
            # Handle errors or log error messages here
            pass
