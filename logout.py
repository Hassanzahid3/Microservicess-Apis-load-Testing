from locust import HttpUser, task, between

class LogoutUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def logout(self):
        headers = {
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send the POST request for logout
        response = self.client.post("/v1/auth/private/logout", headers=headers)

        if response.status_code == 200:
            print("Logout successful")
        else:
            print("Logout failed")

