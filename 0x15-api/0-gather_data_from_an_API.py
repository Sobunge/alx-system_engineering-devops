#!/usr/bin/python3

import sys
import requests


def get_employee_todo_progress(employee_id):
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
