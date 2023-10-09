from locust import HttpUser, task, between

class RegistrationUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def register_user(self):
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "email": "abdullah.ahmed@imlink.network",
            "username": "abdullah.ahmad01",
            "fullName": "Abdullah Ahmad",
            "password": "Password1@#",
            "confirmPassword": "Password1@#",
            "gender": "2",
            "phone": "+923244545555",
            "dateOfBirth": "16-03-2000",
            "deviceId": "123456009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348009665495342b348",
            "deviceType": "IOS",
            "osVersion": "30.1"
        }

        response = self.client.post(
            "/v1/users/public/register",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            # Registration successful
            pass
        else:
            # Handle the response when registration fails (e.g., logging or reporting)
            pass
