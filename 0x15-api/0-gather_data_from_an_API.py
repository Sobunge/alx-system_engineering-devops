#!/usr/bin/python3
"""
Retrieves information about an employee's TODO list progress using a REST API.
"""

import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_data)
        done_tasks = sum(1 for task in todo_data if task["completed"])

        # Display progress
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in todo_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
