from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Initialize the database connection
engine = create_engine("sqlite:///passwords.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

#defining the function
def add_password(account, password):
    #creating a session
    session = Session()
    #the new password should consist of an account and a password
    new_password = Password(account=account, password=password)
    #then you it adds itself
    session.add(new_password)
    session.commit()
    session.close()

#defining the function
def get_password(account):
    #create a session
    session = Session()
    #We use filter.method to get all the passwords in order
    password = session.query(Password).filter_by(account=account).first()
    session.close()
    #If password it will return itself
    return password.Password if password else None#and return None if its not a password

#defining the function
def list_accounts():
    #creating a session
    session = Session()
#we want to have all the account in a list
    accounts = session.query(Password.account).all()
    session.close()
    #it will return starting with the account in the zero index(the first index)
    return [account[0] for account in accounts]


#defining the delete function
def delete_password(account):
    session = Session()
    #to delete the password we filter and check if it matches with its account deletes in order
    password = session.query(Password).filter_by(account=account).first()
#if its that password it deletes commit and close and prints:
    if password:
        session.delete(password)
        session.commit()
        session.close()
        print("Deleted password for {}.".format(account))
        #if not it prints the following
    else:
        session.close()
        print("No password found for {}. Nothing deleted.".format(account))

