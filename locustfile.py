from locust import HttpLocust, TaskSet, task

import resource

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        response = self.client.post("/api-token-auth/", {"username": "admin@tweetcheck.com", "password": "admin"})
        self.client.headers.update({'Authorization': 'Token {0}'.format(response.json()['token'])})

    @task(5)
    def view_dashboard(self):
        self.client.get("/api/tweets/")

    @task(2)
    def view_detail(self):
        self.client.get("/api/tweets/1/")

    @task(1)
    def new_tweet(self):
        self.client.post("/api/tweets/", {'handle': 1, 'body': 'This tweet brought to you by Locust'})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'http://192.168.59.103:8000'
    # host = 'http://www.tweetcheck.com'
    min_wait = 5000
    max_wait = 9000
