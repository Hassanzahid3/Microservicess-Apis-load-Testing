from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # You can customize the wait time between requests here
    host = "https://staging.imlink.network"  # Define the base URL

    @task
    def update_profile(self):
        endpoint = "/v1/users/private/profile"
        payload = {
            "fullName": "Linker Khan Ji"
        }

        headers = {
            "Content-Type": "application/json",
            "Content-Length": "172",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send the PUT request
        response = self.client.put(endpoint, json=payload, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            # Request was successful, you can handle the response here
            # assertions or log the response here if needed
            pass
        else:
            # Log that the request was not successful
            self.log.info(f"Request failed with status code {response.status_code}")
