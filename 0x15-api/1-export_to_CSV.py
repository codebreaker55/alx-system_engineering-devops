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
    todos_req = requests.get(url + "todos", params={"userId": user_id}, verify=False).json()

# Write user's todo items to a CSV file with their user ID as the filename
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, t.get("completed"), t.get("title")]
         ) for t in todos_req]
