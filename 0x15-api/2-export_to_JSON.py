#!/usr/bin/python3
"""
extend Python script to export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    todo_url = url + "todos"
    todo_params = {"userId": user_id}
    todos_req = requests.get(todo_url, params=todo_params).json()

    user_data = {user_id: []}
    for todo in todos_req:
        TASK_COMPLETED_STATUS = todo.get('completed')
        TASK_TITLE = todo.get('title')
        user_data[user_id].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": user_name})

    # print the user_data using json
    with open('{}.json'.format(user_id), 'w') as j:
        json.dump(user_data, j)
