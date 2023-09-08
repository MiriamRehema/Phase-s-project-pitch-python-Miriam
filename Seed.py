from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Password

# Initialize the database connection
engine = create_engine("sqlite:///passwords.db")
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)

def seed_database():
    # Create a session
    session = Session()

    # Define the initial data you want to insert into the database
    initial_data = [
        {"account": "Miriam", "password": "659556"},
        {"account": "Rehema", "password": "fur677"},
        {"account": "Irungu", "password": "jhfyk6545"},
        {"account": "Hellen", "password": "659556"},
        {"account": "Jane", "password": "fur677"},
        {"account": "Hadassah", "password": "jhfyk6545"},
        {"account": "James", "password": "659556"},
        {"account": "Wilson", "password": "fur677"},
        {"account": "Ruth", "password": "jhfyk6545"},
        {"account": "Joseph", "password": "659556"},
        {"account": "Malkia", "password": "fur677"},
        {"account": "Evan", "password": "jhfyk6545"},
        {"account": "Westly", "password": "659556"},
        {"account": "George", "password": "fur677"},
        {"account": "Cory", "password": "jhfyk6545"},
        {"account": "Duke", "password": "659556"},
        {"account": "Mary", "password": "fur677"},
        {"account": "Houston", "password": "jhfyk6545"},
    ]

    # Insert the initial data into the database
    for data in initial_data:
        new_password = Password(account=data["account"], password=data["password"])
        session.add(new_password)

    # Commit the changes and close the session
    session.commit()
    session.close()
    

if __name__ == "__main__":
    # Call the seed_database function to insert the initial data
    seed_database()
    print("Database seeded successfully.")
