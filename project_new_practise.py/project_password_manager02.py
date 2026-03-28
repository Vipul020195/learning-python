import json
import os
from cryptography.fernet import Fernet

PASSWORD_FILE = "passwords.json"
KEY_FILE = "key.key"

def load_password():
    if os.path.exists(PASSWORD_FILE):
        with open('PASSWORD_FILE', 'r') as f:
            return json.load(f)
    return{}

