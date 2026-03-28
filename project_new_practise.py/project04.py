import json
import os
from cryptography.fernet import Fernet

# File to store passwords
PASSWORD_FILE = "passwords.json"
KEY_FILE = "key.key"

def load_or_create_key():
    """Load encryption key or create a new one"""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key

def load_passwords():
    """Load passwords from file"""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_passwords(passwords):
    """Save passwords to file"""
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f, indent=4)

def encrypt_password(password, key):
    """Encrypt password"""
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    """Decrypt password"""
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()

def add_password(service, username, password, key):
    """Add a new password"""
    passwords = load_passwords()
    encrypted_pwd = encrypt_password(password, key)
    passwords[service] = {"username": username, "password": encrypted_pwd}
    save_passwords(passwords)
    print(f"✓ Password for {service} saved!")

def retrieve_password(service, key):
    """Retrieve a password"""
    passwords = load_passwords()
    if service in passwords:
        encrypted_pwd = passwords[service]["password"]
        decrypted_pwd = decrypt_password(encrypted_pwd, key)
        print(f"Service: {service}")
        print(f"Username: {passwords[service]['username']}")
        print(f"Password: {decrypted_pwd}")
    else:
        print(f"No password found for {service}")

def list_services():
    """List all saved services"""
    passwords = load_passwords()
    if passwords:
        print("\nSaved Services:")
        for service in passwords.keys():
            print(f"  - {service}")
    else:
        print("No passwords saved yet")

def main():
    key = load_or_create_key()
    
    while True:
        print("\n--- Password Manager ---")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. List Services")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            service = input("Service name: ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(service, username, password, key)
        
        elif choice == '2':
            service = input("Enter service name: ")
            retrieve_password(service, key)
        
        elif choice == '3':
            list_services()
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()