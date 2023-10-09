from locust import HttpUser, task, between

class OtpVerify(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task
    def otp_verify(self):
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",  # Set the Content-Length header
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "email": "linker1",
            "otp": "8567"
        }

        response = self.client.patch(
            "/v1/auth/public/register/otp-verify",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            # You can add your verification or validation logic here
            pass
        else:
            # Handle the response when it's not 200 (e.g., logging or reporting)
            pass
