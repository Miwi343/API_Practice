import requests
from typing import Optional, Dict, Any

BASE_URL = "https://reqres.in/api"

def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    """GET a user by ID. Return JSON dict if success, else None."""
    url = f"{BASE_URL}/users/{user_id}"
    # TODO: use requests.get(url), check status_code, return parsed JSON
    pass

def create_user(name: str, job: str) -> Optional[Dict[str, Any]]:
    """POST to create a new user. Return response JSON if created, else None."""
    url = f"{BASE_URL}/users"
    payload = {"name": name, "job": job}
    # TODO: use requests.post(url, json=payload), check status_code, return parsed JSON
    pass

def update_user(user_id: int, name: str, job: str) -> Optional[Dict[str, Any]]:
    """PUT to update user. Return JSON if OK, else None."""
    url = f"{BASE_URL}/users/{user_id}"
    payload = {"name": name, "job": job}
    # TODO: use requests.put(url, json=payload), check status_code, return parsed JSON
    pass

def delete_user(user_id: int) -> bool:
    """DELETE a user. Return True if success, else False."""
    url = f"{BASE_URL}/users/{user_id}"
    # TODO: use requests.delete(url), check if status_code == 204
    pass

def main():
    """Simple test harness to call your functions and print results."""

    print("== GET user with id=2")
    user = get_user(2)
    print(user)

    print("\n== CREATE user")
    new = create_user("Alice", "Engineer")
    print(new)

    print("\n== UPDATE user with id=2")
    updated = update_user(2, "Bob", "Manager")
    print(updated)

    print("\n== DELETE user with id=2")
    deleted = delete_user(2)
    print("Deleted:", deleted)


if __name__ == "__main__":
    main()
