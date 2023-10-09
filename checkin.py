from locust import HttpUser, task, between

class CheckInUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def check_in(self):
        endpoint = "/v1/places/private/checkin/4b98ccf1f964a520235035e3/users?page-number=1&items-per-page=1"

        headers = {
            "Content-Type": "application/json",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "fsqId": "4b98ccf1f964a520235035e3",
            "latitude": 31.373669,
            "longitude": 74.181947,
            "name": "Food Court Bahria Test3",
            "category": "Cafe",
            "userCount": 1
        }

        response = self.client.post(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Check-In Successful")
        else:
            self.log.error("Check-In Failed")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")  # Replace with the name of your Locust file
