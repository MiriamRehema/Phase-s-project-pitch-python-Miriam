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

def add_password(account, password):
    session = Session()
    new_password = Password(account=account, password=password)
    session.add(new_password)
    session.commit()
    session.close()

def get_password(account):
    session = Session()
    password = session.query(Password).filter_by(account=account).first()
    session.close()
    return password.password if password else None

def list_accounts():
    session = Session()
    accounts = session.query(Password.account).all()
    session.close()
    return [account[0] for account in accounts]

def delete_password(account):
    session = Session()
    password = session.query(Password).filter_by(account=account).first()

    if password:
        session.delete(password)
        session.commit()
        session.close()
        print("Deleted password for {}.".format(account))
    else:
        session.close()
        print("No password found for {}. Nothing deleted.".format(account))

