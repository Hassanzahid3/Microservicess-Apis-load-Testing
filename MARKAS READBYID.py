from locust import HttpUser, task, between

class Notifications(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def mark_notification_as_read(self):
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        # Replace 'ab13ad88-64ec-4227-a245-186a48d46c99' with the actual notification ID you want to mark as read
        notification_id = "ab13ad88-64ec-4227-a245-186a48d46c99"

        response = self.client.put(
            f"/v1/notifications/private/mark-as-read/{notification_id}",
            headers=headers
        )

        if response.status_code == 200:
            pass  # Handle a successful response (status code 200) if needed
        else:
            pass  # Handle an unsuccessful response if needed
