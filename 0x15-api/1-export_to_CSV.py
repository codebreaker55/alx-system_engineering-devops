#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""
import csv
import requests
import sys
import urllib3


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id), verify=False).json()
    user_name = user.get("username")
    todo = (url + "todos", params={"userId": user_id}, verify=False)
    todos_req = requests.get(todo).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, t.get("completed"), t.get("title")]
         ) for d in todos_req]
