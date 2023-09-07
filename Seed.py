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
