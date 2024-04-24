#!/usr/bin/python3
"""
Retrieves information about an employee's TODO list progress from a REST API.
"""

import requests
import sys

USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def get_employee_info(employee_id):
    """
    Retrieves information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch user name
    resp_users = requests.get(USERS_URL)
    users_data = resp_users.json()

    employee_name = None
    for user in users_data:
        if user.get('id') == employee_id:
            employee_name = user.get('name')
            break

    if not employee_name:
        print(f"No employee found with ID {employee_id}")
        return

    # Fetch todos
    resp_todos = requests.get(TODOS_URL, params={'userId': employee_id})
    todos_data = resp_todos.json()

    # Count completed and total tasks
    completed_tasks = [todo for todo in todos_data if todo.get('completed')]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # Print employee info
    print(f"First line: Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
    print(f"{employee_name}:")

    # Print completed tasks
    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_info(employee_id)
