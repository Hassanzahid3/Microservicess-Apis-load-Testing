from locust import HttpUser, task, between

class UpdateCommentUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def update_comment(self):
        endpoint = "/v1/comments/private/comment/7484d235-0493-4e70-8e58-855702185f92"

        headers = {
            "Content-Type": "application/json",
            "Host": "staging.imlink.network",
            "User-Agent": "Locust",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "comment": "good job v good",
            "commentType": "gif"
        }

        response = self.client.put(endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            self.log.info("Update Comment Successful")
        else:
            self.log.error("Update Comment Failed")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")  # Replace with the name of your Locust file
