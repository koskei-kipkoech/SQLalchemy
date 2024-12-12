from model import db,User,Account
from sqlalchemy.orm import joinedload
#run our app

#create our app
user = User(first_name="john", email="john@example.com", phone="0722323232")
#add the user instance to the db transaction
# db.add(user)
# commit the transaction
# db.commit()

account = Account(user_id=1,working_balance=100, balance=500, credit_score=200)
# db.add(account)
# db.commit()

#read
# users = db.query(User).all()
#for u in users:
#print(users)

#retrieve a single record using a specific column 

user = db.query(User).options(joinedload(User.accounts)).filter(User.id == 1 ).first()
print(user)

#update
#1. retrive that record 
# user2 = db.query(User).filter(User.id == 1).first()

#update the necessary fields
# user2.phone = "0722123213"
#ru  the delete method db
# db.add(user2)
#commit the transaction
# db.commit()



#deleting
# user3 = db.query(User).filter(User.id == 2).first()
# db.delete(user3)
# db.commit()