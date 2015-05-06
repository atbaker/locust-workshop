from locust import HttpLocust, TaskSet, task

import resource

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()
        resource.setrlimit(resource.RLIMIT_NOFILE, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
        self.client.headers.update({'Authorization': 'Token 7cdfaa69c2986c0e4c631ba4338c6eed146bb34b'})

    # def login(self):
    #     self.client.post("/admin/login", {"username":"admin@tweetcheck.com", "password":"admin"})

    @task(2)
    def index(self):
        self.client.get("/api/tweets")

    @task(1)
    def profile(self):
        self.client.get("/api/tweets/1")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'http://192.168.59.103:8000'
    min_wait = 5000
    max_wait = 9000
