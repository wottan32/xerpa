from locust import HttpUser, task, between
import json
import random
import uuid

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)  # Tiempo de espera entre cada tarea

    @task
    def post_transactions(self):
        transactions = [
            {
                "id": str(uuid.uuid4()),
                "description": "Test Transaction {}".format(i),
                "amount": random.uniform(-500, 500),
                "date": "2023-12-01"
            }
            for i in range(1000)
        ]
        self.client.post("/api/enrich/", json=transactions, headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")
