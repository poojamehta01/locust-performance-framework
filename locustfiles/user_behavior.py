import random
import json
from locust import HttpUser, task, between
from utils.helpers import load_config

class APIUser(HttpUser):
    wait_time = between(1, 3)
    config = load_config()

    def on_start(self):
        """Initialize user session"""
        self.base_url = self.config['base_url']
        # No authentication needed for this public API

    @task(3)
    def get_posts(self):
        with self.client.get(self.config['endpoints']['posts'], catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Get posts failed with status code: {response.status_code}")
            else:
                response.success()

    @task(2)
    def get_user(self):
        user_id = random.randint(1, 10)  # JSONPlaceholder has 10 users
        with self.client.get(f"{self.config['endpoints']['users']}/{user_id}", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Get user failed with status code: {response.status_code}")
            else:
                response.success()

    @task(2)
    def create_post(self):
        payload = {
            "title": "Load Test Post",
            "body": "This is a test post created during load testing",
            "userId": random.randint(1, 10)
        }
        with self.client.post(
            self.config['endpoints']['posts'],
            json=payload,
            catch_response=True
        ) as response:
            if response.status_code != 201:  # JSONPlaceholder returns 201 for successful creation
                response.failure(f"Create post failed with status code: {response.status_code}")
            else:
                response.success()

    @task(1)
    def get_comments(self):
        post_id = random.randint(1, 100)  # JSONPlaceholder has 100 posts
        params = {"postId": post_id}
        with self.client.get(
            self.config['endpoints']['comments'],
            params=params,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Get comments failed with status code: {response.status_code}")
            else:
                response.success()
