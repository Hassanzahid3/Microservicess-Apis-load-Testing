from locust import HttpUser, task, between

class DeleteCommentUser(HttpUser):
    host = "https://staging.imlink.network"
    wait_time = between(1, 3)

    @task(1)
    def delete_comment(self):
        endpoint = "/v1/comments/private/comment/7484d235-0493-4e70-8e58-855702185f92"

        headers = {
            "Host": "staging.imlink.network",
            "User-Agent": "PostmanRuntime/7.33.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = self.client.delete(endpoint, headers=headers)

        if response.status_code == 204:
            self.log.info("Delete Comment Successful")
        else:
            self.log.error("Delete Comment Failed")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")  # Replace with the name of your Locust file
