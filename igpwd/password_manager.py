import json
import os 
from cryptography.fernet import Fernet
from dotenv import load_dotenv

#Load encryption key from .env
load_dotenv()
key = os.getenv("ENCRYPTION_KEY")

if not key:
    raise ValueError("Encryption key not found. Generate it first with generate_key.py")

cipher = Fernet(key.encode())

def save_password(password):
    # Encrypt and save password to a file 
    encrypted_password = cipher.encrypt(password.encode()).decode

    data = {"instagram password": encrypted_password}

    with open("secrets.json", "w") as f:
        json.dump(data, f)

    print("Password saved securely")

def retrieve_password():
    #Retrieve and decrypt password
    try:
        with open ("secrets.json", "r") as f:
            data = json.load(f)
            encrypted_password = data["instagram password"]
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            return decrypted_password
    except FileNotFoundError:
        print("No password stored.")
        return None 