from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Customer(db.Model):
    __tablename__='customers'
    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name= db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(225),nullable=False)
    address=db.Column(db.String(300),nullable=False)
    city=db.Column(db.String(70),nullable=False)
    state=db.Column(db.String(10),nullable=False)
    zip=db.Column(db.String(10),nullable=False)
    
    def __init__(self,first_name,last_name,email,address,city,state,zip):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        

    def serialize(self):
        return{
            "ID:":self.id,
            "First_Name":self.first_name,
            "Last_Name":self.last_name,
            "Email":self.email,
            "Street_Address":self.address,
            "City":self.city,
            "State":self.state,
            "Zip":self.zip,
        }

