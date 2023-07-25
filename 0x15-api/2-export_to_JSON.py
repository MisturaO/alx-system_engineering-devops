#!/usr/bin/python3
"""
This script fetches data from a REST API and stores
the data fetched into a file in JSON format.

The script must accept an integer as a parameter, which is the employee ID
"""
import json
import requests
import sys

if __name__ == "__main__":
    # stores the user's ID passed as argument to the script on cmd line
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    # adds the user's ID to the endpoint url of the API users resource
    users = requests.get(base_url + "users/{}".format(user_id)).json()
    # adds the user's ID to the endpoint url of the API todo resource
    todos = requests.get(base_url + "todos/",
                         params={"userId": user_id}).json()

    # writes into a .json file format(file name will be an
    # # int arg passed to the script on cmd line)
    with open("{}.json".format(user_id), "w") as jsonfile:
        # stores the required data into the json file(jsonfile)
        # as valid json properties and values
        json.dump({user_id: [{"task": todo.get("title"),
                  "completed": todo.get("completed"),
                             "username": users.get("username")}
                             for todo in todos]}, jsonfile)
