# to run make sure you cd server
# to run client, cd .. , then cd client
# while in flask_app run .\env\Scripts\Activate.ps1 to activate enviorment
#cors has issue with 5000

from random import randint
from flask import Flask, jsonify 
from flask_cors import CORS
from sqlalchemy import create_engine, ForeignKey , Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    ssn = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    gender = Column('geder', CHAR)
    age = Column('age', Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    
    def __repr__(self):
        return f'({self.ssn}){self.firstname} {self.lastname} ({self.gender}, {self.age})'
    
engine = create_engine('sqlite:///mydb.db',echo = True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(1234, "Mike", 'Smith', "M", 30)
session.add(person)
session.commit()

person1 = Person(6786, "Msoh", 'Mossy', "M", 23)
person2 = Person(8709, "Julia", 'Loss', "F", 34)
person3 = Person(3463, "Rick", 'Giordano', "M", 19)
person4 = Person(3345, "Sam", 'Simmon', "F", 27)


app = Flask(__name__)
CORS(app)

# Run: python server.py , and go to localhost:(number)'/api/home' == num run dev
@app.route('/api', methods=['GET'])
def return_home():
    return jsonify({
        'message':'Hello World from the backend',
        'people': ['Jack','Sam','Tom','Jeffery','Aldi'],
        'number':randint(1,30)
    })

if __name__ == '__main__':
    app.run(debug=True,port=8080)
