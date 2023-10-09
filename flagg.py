from locust import HttpUser, task, between

class GetFollowers(HttpUser):
    host = "https://staging.imlink.network"
    endpoint = "/v1/users/private/follower?page-number=1&items-per-page=20"
    wait_time = between(1, 3)

    def on_start(self):
        # Get user input for the flag (1 or 2)
        flag_input = input("Enter the flag (1 or 2): ")

        if flag_input == "1":
            self.flag = 1
        elif flag_input == "2":
            self.flag = 2
        else:
            print("Invalid flag. Please enter 1 or 2.")
            self.flag = 0  # Set flag to 0 to indicate an invalid input

    # You can define more tasks to simulate different user behaviors
    @task
    def get_followers(self):
        if self.flag == 1:
            response = self.client.get(f"{self.host}{self.endpoint}")

            # Check response status code and handle accordingly
            if response.status_code == 200:
                # Successful response handling here
                pass
            else:
                # Handle other responses here
                pass
        elif self.flag == 2:
            print("Flag is set to 2. Code will not execute.")
        else:
            print("Invalid flag. Code will not execute.")

