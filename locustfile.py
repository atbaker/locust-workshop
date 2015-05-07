from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        """ special locust method - called before any other tasks are scheduled """
        self.login()

    def login(self):
        # Get a token so our locusts can use the API
        response = self.client.post("/api-token-auth/", {"username": "admin@tweetcheck.com", "password": "admin"})
        self.client.headers.update({'Authorization': 'Token {0}'.format(response.json()['token'])})

    @task
    def view_api_root(self):
        self.client.get("/api/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = '' # Substitute your TweetCheck server's hostname here
    min_wait = 5000
    max_wait = 10000
