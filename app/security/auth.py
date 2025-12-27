class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "staff": {"password": "staff123", "role": "staff"},
    "viewer": {"password": "viewer123", "role": "viewer"},
}


def authenticate_user():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in USERS and USERS[username]["password"] == password:
        return User(username, USERS[username]["role"])

    raise PermissionError("Invalid username or password")
