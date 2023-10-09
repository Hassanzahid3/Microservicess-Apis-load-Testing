from locust import HttpUser, task, between

class Notifications(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def mark_notification_as_clicked(self):
        headers = {
            "content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        notification_id = " "  # Replace with the actual notification ID you want to mark as clicked

        response = self.client.put(
            f"/v1/notifications/private/mark-as-clicked/{notification_id}",
            headers=headers
        )

        if response.status_code == 204:
            pass  # Handle a successful response (status code 204) if needed
        else:
            pass  # Handle an unsuccessful response if needed
