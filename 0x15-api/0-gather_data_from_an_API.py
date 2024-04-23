#!/usr/bin/python3
"""
Checks student output for returning TODO list progress from REST API
"""

import requests
import sys

USERS_URL = "https://jsonplaceholder.typicode.com/users"


def get_employee_name(user_id):
    """
    Fetches the name of the employee with the given ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        str: The name of the user if found, None otherwise.
    """
    try:
        response = requests.get(USERS_URL)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        users_data = response.json()

        for user in users_data:
            if user['id'] == user_id:
                return user['name']
        
        print("User ID not found in API response.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        return None


def check_student_output(user_id, output_filename):
    """
    Checks if the student output contains the employee's name.

    Args:
        user_id (int): The ID of the user.
        output_filename (str): The filename of the student's output.

    Returns:
        None
    """
    employee_name = get_employee_name(user_id)
    if employee_name is None:
        print("Employee name not found.")
        return

    with open(output_filename, 'r') as f:
        first_line = f.readline().strip()

    if employee_name in first_line:
        print("Employee Name: OK")
    else:
        print("Employee Name: Incorrect")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <employee_id> <student_output_file>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    output_filename = sys.argv[2]
    check_student_output(user_id, output_filename)
