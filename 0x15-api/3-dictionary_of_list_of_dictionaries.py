#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    USERS = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            us.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": us.get("username")
            } for todo in requests.get(url + "todos",
                                       params={"userId": us.get("id")}).json()]
            for us in USERS}, json_file)
