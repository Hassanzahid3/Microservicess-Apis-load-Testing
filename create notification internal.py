from locust import HttpUser, task, between

class Notifications(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def create_notification_internal(self):
        headers = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        payload = {
            "contentId": "469b24fd-18a2-46d2-a844-bb8cbc569458",
            "useridSender": "469b24fd-18a2-46d2-a844-bb8cbc569458",
            "useridReceiver": "9308254c-c312-455b-848e-ddb462b7cf9a",
            "usernameSender": "salman",
            "usernameReceiver": "Fahad",
            "contentType": "post",
            "senderThumbnail": "somethumbnail",
            "customMessage": "hello",
            "deviceIdReceiver": "f3iDt-mFQger9oMb-MWb-J:APA91bHa8bRxCeWmdN6x_l1YdN7A6f3jnFe7Vil5hq1mX0hd0N0lII7jCirD4Fee0i3boZJZb-fqhgKnnYBszR3RkbWTn9IGAWLtJXTDkFhxrnzrClMWbbrdQjw5Hfydl6Y5HJx-5QBG",
            "deviceTypeReceiver": "android",
            "isReceiverFollower": False
        }

        response = self.client.post(
            "/v1/notifications/private/user-notifications",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            pass  # Handle a successful response if needed
        else:
            pass  # Handle an unsuccessful response if needed
