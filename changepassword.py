from locust import HttpUser, task, between


class changepassword(HttpUser):
    host = "https://staging.imlink.network"  # Update the host URL as needed
    wait_time = between(1, 3)  # Adjust the wait time as needed


@task(13)
def change_password(self):
    # Define the payload
    payload = {
        "currentPassword": "test12345",
        "newPassword": "test12345678",
        "confirmNewPassword": "test12345678"
    }

    # Define the headers
    headers = {
        "Host": "staging.imlink.network",
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.33.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    # Perform the PUT request to change the password
    response = self.client.put("/users/private/change-password", headers=headers)

    if response.status_code == 200:
        print("Password changed successfully")
    else:
        print(f"Password change failed with status code: {response.status_code}")
        print(response.text)  # Print the response text for debugging
