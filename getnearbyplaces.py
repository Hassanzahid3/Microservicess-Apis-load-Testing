from locust import HttpUser, task, between

class GetNearbyPlacesUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def get_nearby_places(self):
        endpoint = "/v1/places/private/places?lat=31.3695&long=74.1768&items-per-page=2"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET Nearby Places Successful")
        else:
            self.log.error("GET Nearby Places Failed")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")  # Replace with the name of your Locust file
