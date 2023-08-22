import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # if you want to track changes set this to true

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):


   __tablename__ = 'puppies' # Manual table name  ,by default it will be as per class name


   ## register table  fileds


   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.Text)
   age = db.Column(db.Integer)
   breed = db.Column(db.Text)


   def __init__(self,name,age,breed):
       self.name = name
       self.age = age
       self.breed = breed


   ##__repr__ give
   def __repr__(self):
       # This is the string representation of a puppy in the model
       return f"Puppy {self.name} is {self.age} years old."

