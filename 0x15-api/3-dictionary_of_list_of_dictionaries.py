#!/usr/bin/python3
"""
This script fetches data from a REST API and stores
the data fetched into a file in JSON format.

The script fetches dictionary of list of dictionaries
of all tasks from all employees.
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    # adds the user's ID to the endpoint url of the API users resource
    users = requests.get(base_url + "users/").json()

    # writes into a .json file format(file name will be an
    # # int arg passed to the script on cmd line)
    with open("todo_all_employees.json", "w") as jsonfile:
        # stores the required data into the json file(jsonfile)
        # as valid json properties and values
        json.dump({
            user.get("id"): [{
                       "task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": user.get("username")
                   }for t in requests.get(base_url + "todos/",
                                          params={"userId":
                                                  user.get("id")}).json()]
            for user in users}, jsonfile)
