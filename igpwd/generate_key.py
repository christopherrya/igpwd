from cryptography.fernet import Fernet 

# Generate new encryption key 
key = Fernet.generate_key()

with open(".env", "w") as f:
    f.write(f"ENCRYPTION_KEY={key.decode()}\n")

print("Encryption key generated and store in .env file")