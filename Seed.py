from model import add_password
from sqlalchemy.exc import IntegrityError
from cryptography.fernet import Fernet, InvalidToken

# Encryption key (replace with your own secret key)
ENCRYPTION_KEY = b'your_secret_key_here'

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode())

# Sample data to seed the database (encrypted)
sample_data = [
    {"account": "example1.com", "password": "password1"},
    {"account": "example2.com", "password": "password2"},
    {"account": "example3.com", "password": "password3"},
]

def seed_database():
    for data in sample_data:
        account = data["account"]
        password = data["password"]

        # To demonstrate deletion, uncomment the following line
        # delete_password(account)
        # print(f"Deleted {account} from the database.")

        try:
            encrypted_password = encrypt_data(password, ENCRYPTION_KEY)
            add_password(account, encrypted_password)
            print("Added {} to the database".format(account))

        except IntegrityError:
          print("{} already exists in the database. Skipping.".format(account))

        except InvalidToken:
           print("Failed to encrypt {}'s password. Skipping.".format(account))
if __name__ == "__main__":
    seed_database()
