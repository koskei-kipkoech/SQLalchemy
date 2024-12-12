#define the tables using OOP + SQLalchemy
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine ,Column, Integer, Text, VARCHAR, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship



#connect to db using sessionmaker(similar to sqlite conn)
engine  = create_engine("sqlite:///app.db", echo=True)

#create session maker
Session = sessionmaker(bind=engine)
db = Session()

#create a base model that all models are going to inherit from
Base = declarative_base()

#define the User model
"""
1. its a must we provide the table name via the attribute __tablename__
2. provide at least one table column.
"""
class User(Base):
    __tablename__ = 'users'

    #define colums
    id = Column(Integer(), primary_key=True)
    first_name = Column(Text(), nullable=False) #not null
    email = Column(VARCHAR(), nullable=False, unique=True) #not null and unique
    phone = Column(Integer(), nullable=True ) #not null and unique
#one to many
    accounts = relationship("Account" , backref="user")

    def __repr__(self):
        accounts_length = len(self.accounts)
        return f'<User({self.id}, first_name={self.first_name}, email={self.email}, phone={self.phone}, Accounts: {self.accounts})>'

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer(), primary_key=True)
    working_balance = Column(Integer())
    balance = Column(Integer())
    credit_score = Column(Integer())
    user_id = Column(Integer(), ForeignKey("users.id"))
#many to one relationship
    #user = relationship("User",backref="accounts", uselist=False)
    #timestamp 
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime())

    def __repr__(self):
        return f'(Account {self.id}, working_balance={self.working_balance}, balance={self.balance}, credit_score={self.credit_score}, user_id={self.user_id}, created_at={self.created_at}, updated_at={self.updated_at})'


