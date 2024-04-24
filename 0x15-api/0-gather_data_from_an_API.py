#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
from a REST API and displays it in a specific format.

Usage:
    python3 gather_data_from_an_API.py <employee_id>

Arguments:
    employee_id: An integer representing the ID of the employee whose
                 TODO list progress needs to be retrieved.

Requirements:
    - The script must use the urllib or requests module.
    - The script must display the employee's TODO list progress in the
      specified format.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetches information about the employee's TODO list progress from the
    REST API and prints it in the specified format.

    Args:
        employee_id (int): The ID of the employee whose TODO list progress
                           needs to be retrieved.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    employee_name = user_data.get('name', 'Unknown')
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
