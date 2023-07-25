#!/usr/bin/python3
"""
This script gathers data from an API using this REST API
(https://jsonplaceholder.typicode.com/),for a given employeeID,
returns information about his/her TODO list progress.

This script accepts an integer as a parameter, which is the employee ID
"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base_url + "todos",
                        params={"userId/{}": sys.argv[1]}).json()
    completed_todo = [todo.get("title") for todo in todos if
                      todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(users.get("name"), len("completed"), len("todos")))
    [print("\t {}".format(c)) for c in completed_todo]
