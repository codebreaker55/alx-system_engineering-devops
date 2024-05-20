#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import re
import requests
import sys


REST_API = " https://jsonplaceholder.typicode.com/ "
"""the required RESET API URL"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            usr_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            todo_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = usr_req.get('name')
            tasks_no = list(filter(lambda x: x.get('userId') == id, todo_req))
            done_tasks = list(filter(lambda x: x.get('completed'), tasks_no))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(done_tasks),
                    len(tasks_num)
                )
            )
            for task_done in done_tasks:
                print('\t {}'.format(task_done.get('title')))
