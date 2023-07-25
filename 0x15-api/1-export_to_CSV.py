#!/usr/bin/python3
"""
This script fetches a given employee's(ID) todo
list information and stores it to a file in CSV format.

The script takes a CMD line arg which is the employee's ID and
uses the arg(which is an interger) to create the file name in csv format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(user_id)).json()
    username = users.get("username")
    todos = requests.get(base_url + "todos",
                         params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, todo.get("completed"),
                          todo.get("title")]) for todo in todos]
