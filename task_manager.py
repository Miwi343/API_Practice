import requests
import sys
from typing import Optional, Dict, Any, List

BASE_URL = "https://reqres.in/api"

# Local in-memory task store
# Structure: { user_id: [ { "task_id": int, "title": str, "description": str, "completed": bool } ] }
tasks_store: Dict[int, List[Dict[str, Any]]] = {}
next_task_id = 1  # for generating unique local task IDs


def list_users(page: int = 1) -> Optional[List[Dict[str, Any]]]:
    """
    Fetch users list from ReqRes for given page.
    Return list of user dicts, or None if error.
    """
    url = f"{BASE_URL}/users"
    params = {"page": page}
    # TODO: make GET request, handle response, return list of users
    pass


def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch a single user by ID.
    Return user dict if exists, else None.
    """
    url = f"{BASE_URL}/users/{user_id}"
    # TODO: GET, check for 404 / other errors, parse JSON
    pass


def create_user(name: str, job: str) -> Optional[Dict[str, Any]]:
    """
    Create a new user via ReqRes.
    Return dict with created user info (id, createdAt, etc.) or None if error.
    """
    url = f"{BASE_URL}/users"
    data = {"name": name, "job": job}
    # TODO: POST, parse JSON, return result
    pass


def update_user(user_id: int, name: Optional[str] = None, job: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Update existing user’s name/job fields.
    Return dict with updated info or None if user not exists or error.
    """
    url = f"{BASE_URL}/users/{user_id}"
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if job is not None:
        data["job"] = job
    # TODO: PUT or PATCH, handle errors, return result
    pass


def delete_user(user_id: int) -> bool:
    """
    Delete a user by ID.
    Return True if deletion succeeded (e.g. status code 204), False otherwise.
    """
    url = f"{BASE_URL}/users/{user_id}"
    # TODO: DELETE, check response status
    pass


# TASKS (local)

def add_task(user_id: int, title: str, description: str) -> Optional[Dict[str, Any]]:
    """
    Add a task locally for the user_id.
    If user does not exist in ReqRes, return None.
    Otherwise return the task dict.
    """
    global next_task_id
    # TODO: verify user exists (call get_user)
    # TODO: create task dict, update tasks_store
    pass


def list_tasks(user_id: int) -> Optional[List[Dict[str, Any]]]:
    """
    Return list of tasks for user_id. If no tasks or if user not exists, handle appropriately.
    """
    # TODO
    pass


def update_task(user_id: int, task_id: int, title: Optional[str] = None,
                description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
    """
    Update fields of a task. Return True if update succeeds, False if task not found or user invalid.
    """
    # TODO
    pass


def delete_task(user_id: int, task_id: int) -> bool:
    """
    Delete a task. Return True if deleted, False otherwise.
    """
    # TODO
    pass


def delete_user_and_tasks(user_id: int) -> bool:
    """
    Delete user via API and also delete all local tasks for that user.
    Return True if user deletion succeeded and tasks cleaned up (or tasks were none).
    """
    # TODO: call delete_user, and if succeeds, remove tasks from tasks_store if any.
    pass


def main():
    """
    A simple command line interface to test the functions.
    Example usage:
      python task_manager.py list_users
      python task_manager.py get_user 2
      python task_manager.py create_user Alice Engineer
      python task_manager.py add_task 2 "Title" "Desc"
      python task_manager.py list_tasks 2
      ... etc
    """
    # Parse command line args
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command> [args...]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list_users":
        page = 1
        if len(sys.argv) >= 3:
            page = int(sys.argv[2])
        users = list_users(page=page)
        print(users)

    elif command == "get_user":
        if len(sys.argv) < 3:
            print("Usage: get_user <user_id>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        user = get_user(user_id)
        print(user)

    elif command == "create_user":
        if len(sys.argv) < 4:
            print("Usage: create_user <name> <job>")
            sys.exit(1)
        name = sys.argv[2]
        job = sys.argv[3]
        new_user = create_user(name, job)
        print(new_user)

    elif command == "update_user":
        if len(sys.argv) < 3:
            print("Usage: update_user <user_id> [name=<name>] [job=<job>]")
            sys.exit(1)
        user_id = int(sys.argv[2])
        # parse optional args
        name = None
        job = None
        for arg in sys.argv[3:]:
            if arg.startswith("name="):
                name = arg.split("=",1)[1]
            elif arg.startswith("job="):
                job = arg.split("=",1)[1]
        updated = update_user(user_id, name=name, job=job)
        print(updated)

    elif command == "delete_user":
        if len(sys.argv) < 3:
            print("Usage: delete_user <user_id>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        success = delete_user(user_id)
        print(f"Deleted user {user_id}: {success}")

    # Task commands
    elif command == "add_task":
        if len(sys.argv) < 5:
            print("Usage: add_task <user_id> <title> <description>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        title = sys.argv[3]
        description = sys.argv[4]
        task = add_task(user_id, title, description)
        print(task)

    elif command == "list_tasks":
        if len(sys.argv) < 3:
            print("Usage: list_tasks <user_id>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        tasks = list_tasks(user_id)
        print(tasks)

    elif command == "update_task":
        if len(sys.argv) < 4:
            print("Usage: update_task <user_id> <task_id> [title=<title>] [description=<desc>] [completed=<True/False>]")
            sys.exit(1)
        user_id = int(sys.argv[2])
        task_id = int(sys.argv[3])
        title = None
        description = None
        completed = None
        for arg in sys.argv[4:]:
            if arg.startswith("title="):
                title = arg.split("=",1)[1]
            elif arg.startswith("description="):
                description = arg.split("=",1)[1]
            elif arg.startswith("completed="):
                val = arg.split("=",1)[1]
                if val.lower() in ("true", "yes", "1"):
                    completed = True
                elif val.lower() in ("false", "no", "0"):
                    completed = False
        ok = update_task(user_id, task_id, title=title, description=description, completed=completed)
        print(f"Update task {task_id} for user {user_id}: {ok}")

    elif command == "delete_task":
        if len(sys.argv) < 4:
            print("Usage: delete_task <user_id> <task_id>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        task_id = int(sys.argv[3])
        ok = delete_task(user_id, task_id)
        print(f"Deleted task {task_id} for user {user_id}: {ok}")

    elif command == "delete_user_and_tasks":
        if len(sys.argv) < 3:
            print("Usage: delete_user_and_tasks <user_id>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        ok = delete_user_and_tasks(user_id)
        print(f"Delete user {user_id} and tasks: {ok}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
