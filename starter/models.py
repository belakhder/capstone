import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer,ForeignKey
from flask_marshmallow import Marshmallow

database_filename = "test3"

database_path = "postgres://buvrmfmsgtvagl:9503fc794b269b11630ae53c57d18d05e8b4cb2ba517f9e73fe95dca8e2236eb@ec2-54-234-28-165.compute-1.amazonaws.com:5432/d165f6o5r8qn9q"

db = SQLAlchemy()
ma = Marshmallow()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    ma.app=app
    db.init_app(app)
    # db.drop_all()
    db.create_all()


class Account(db.Model):

    id = Column(Integer, primary_key=True)
    first_name= Column(String(50),nullable=False)
    last_name= Column(String(50),nullable=False)
    email=Column(String(100),nullable=False,unique=True)
    phone=Column(String(50),nullable=False)
    addresses=db.relationship('Address',backref='addresses_account')

class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id','first_name','last_name','email','phone')

account_Schema = AccountSchema()
accounts_Schema = AccountSchema(many=True)

class Address(db.Model):
    id = Column(Integer, primary_key=True)
    city=Column(String(50),nullable=False)
    state=Column(String(50))
    postal_code=Column(Integer)
    country=Column(String(50),nullable=False,default='Tunisie')
    account_id=Column(Integer,ForeignKey('account.id'),nullable=False)
  
class AddressSchema(ma.Schema):
    class Meta:
        fields = ('id','city','state','postal_code',
        'country','account_id')

address_Schema = AddressSchema()
addresses_Schema = AddressSchema(many=True)


   