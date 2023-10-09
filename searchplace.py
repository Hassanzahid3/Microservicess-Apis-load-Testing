from locust import HttpUser, task, between

class SearchPlacesUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def search_places(self):
        endpoint = "/v1/places/private/search-places?lat=31.5315&long=74.3679&search=stadium&items-per-page=2"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.get(endpoint, headers=headers)

        if response.status_code == 200:
            self.log.info("GET Search Places Successful")
        else:
            self.log.error("GET Search Places Failed")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")  # Replace with the name of your Locust file
