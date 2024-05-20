#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id), verify=False).json()
    user_name = user.get("username")
    todo_url = url + "todos"
    do_params = {"userId": user_id}
    todos_req = requests.get(todo_url, params=do_params, verify=False).json()

# Write user's todo items to a CSV file with their user ID as the filename
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, t.get("completed"), t.get("title")]
         ) for t in todos_req]
