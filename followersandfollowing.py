import os
from locust import HttpUser, task, between

class MainUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    # Default flag value is 1, can be changed via environment variable
    flag = int(os.getenv("FLAG", 1))  # Set the flag to 2 to disable all tasks

    @task
    def run_all_tasks(self):
        # Check if the flag is set to 1 before executing each task
        if self.flag == 1:
            self.follow_user()
        if self.flag == 1:
            self.unfollow_user()
        if self.flag == 1:
            self.accept_follow_request()
        if self.flag == 1:
            self.remove_follow_request()
        if self.flag == 1:
            self.reject_follow_request()
        if self.flag == 1:
            self.get_followers()
        if self.flag == 1:
            self.get_following()
        if self.flag == 1:
            self.get_following_ids()
        if self.flag == 1:
            self.get_follow_requests()

    def follow_user(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            payload = {
                "userId": "079c81d5-2705-4c99-8683-03dbed0b83ff"
            }

            headers = {"Content-Type": "application/json"}
            response = self.client.post("/v1/users/private/follow", json=payload, headers=headers)

            if response.status_code == 200:
                # Successful response handling here
                pass
            else:
                # Handle other responses here
                pass

    def unfollow_user(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            payload = {"userId": "4a8185bd-a0c3-426f-99df-233f5af19557"}

            headers = {"Content-Type": "application/json"}

            response = self.client.delete("/v1/users/private/unfollow", json=payload, headers=headers)

            if response.status_code == 200:
                pass
            else:
                # Handle other responses here
                pass

    def accept_follow_request(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            payload = {"followRequestId": "cb136675-36d6-44e1-a613-f2566dc6bf1d"}

            headers = {"Content-Type": "application/json"}

            response = self.client.post("/v1/users/private/accept-follow-request", json=payload, headers=headers)

            if response.status_code == 200:
                # Request was successful
                pass
            else:
                # Handle other responses here
                pass

    def remove_follow_request(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            follow_request_id = "9b484be0-2257-43c3-8ff2-aa942806d29e"

            headers = {"Content-Type": "application/json"}
            response = self.client.delete(f"/v1/users/private/remove-follow-request/{follow_request_id}", headers=headers )

            # conditions
            if response.status_code == 204:
                # Successful response handling here (assuming 204 No Content for successful delete)
                pass
            else:
                # Handle other responses here
                pass

    def reject_follow_request(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            payload = {"followRequestId": "9b484be0-2257-43c3-8ff2-aa942806d29e"}

            headers = {
                "Content-Length": "0",
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            response = self.client.put("/v1/user/reject-follow-request", json=payload, headers=headers)

            if response.status_code == 200:
                # Successful response handling here
                pass
            else:
                # Handle other responses here
                pass

    def get_followers(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            response = self.client.get("/v1/users/private/follower?page-number=1&items-per-page=20")

            # response
            if response.status_code == 200:
                # Successful response handling here
                pass
            else:
                # Handle other responses here
                pass

    def get_following(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            response = self.client.get("/v1/users/private/following?page-number=1&items-per-page=5")

            if response.status_code == 200:
                # Successful response handling here
                pass
            else:
                # Handle other responses here
                pass

    def get_following_ids(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*"
            }

            response = self.client.get(
                "/v1/users/private/following-ids",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass

    def get_follow_requests(self):
        # Check if the flag is set to 1 before executing the task
        if self.flag == 1:
            headers = {
                "Host": "staging.imlink.network",
                "User-Agent": "PostmanRuntime/7.33.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            response = self.client.get(
                "/v1/users/private/follow-requests?page-number=1&items-per-page=5",
                headers=headers
            )

            if response.status_code == 200:
                pass
            else:
                pass


if __name__ == "__main__":
    import sys
    from locust import main
    sys.argv = ["locust", "-f", __file__]
    main.main()
