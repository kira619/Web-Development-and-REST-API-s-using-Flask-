from operator import index
from flask import Flask, render_template, request,make_response
from flask import jsonify, redirect,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect,disconnect
from mongoengine import Document, StringField, EmailField ,IntField
#from passwords.fields import PasswordField
#from passwords.validators import (
#    DictionaryValidator, LengthValidator, ComplexityValidator)
from mongoengine.errors import NotUniqueError
import jsonify
from operator import index
from flask import Flask, render_template, request,make_response
from flask import jsonify, redirect,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect,disconnect
from mongoengine import Document, StringField, EmailField
from mongoengine.errors import NotUniqueError,ValidationError


app=Flask(__name__)


connect(db='DemonCyborg',host='127.0.0.1', port=27017)

print("Connected to MongoDB Database.")

#def my_length_check(form, field):
#    if len(field.data) > 50:
#        raise ValidationError('Field must be less than 50 characters')

class user69(Document):
    full_name=StringField(max_length=50)
    email=EmailField(required= True, unique=True)
    mobile_no=IntField(max_length=50)
    password = StringField(required= True,min_length=8,max_length=12)
    confirm_password  = StringField(max_length=50)
    gender = StringField(max_length=50)

    def validate_password(Document, password):
        if len(password.data) < 8 or len(password.data) > 12:
            raise ValidationError('Password must be between 8-12 characters',606)

    def to_json(self):
       #converts this document to JSON
       return{
           "full_name":self.full_name,
           "email":self.email,
           "mobile_no":self.mobile_no,
           "password":self.password,
           "confirm_password":self.confirm_password,
           "gender":self.gender,
       }



#@app.route("/cooldude69", method=['POST']) 
#def add():
#    lomo = {'full_name':request.json['full_name'],
#            'email':request.json['email'],
#            'mobile_no':request.json['mobile_no'],
#            'password':request.json['password'],
#            'confirm_password':request.json['confirm_password'],
#            'gender':request.json['gender']}
#    return jsonify(lomo)
    
@app.route('/populate',methods=['POST'])
def db_populate():
    book = user69(full_name='Tamojit Sarkar')
    book.email='tamojitsarkar619@gmail.com'
    book.mobile_no='9891052574'
    book.password='Welcome@123'
    book.confirm_password='Welcome@123'
    book.gender='Alpha Male'
    book.save()
    return make_response("USER Added.",619)


@app.route('/show_user',methods=['GET'])
def show_users():
   if request.method ==  "GET":
        mylist=[]     
        for x in user69.objects():
            mylist.append(x.to_json())
        return make_response(jsonify(mylist),200)    

@app.route('/add_user',methods=['POST'])
def add_users():
   if request.method == "POST":
    try:
        content = request.json
        book3= user69(full_name=content['full_name'],email=content['email'],mobile_no=content['mobile_no'],
        password=content['password'],confirm_password=content['confirm_password'],gender=content['gender'])
        book3.save()
        return make_response("User Succesfully Added",69)
    except NotUniqueError as nue:
        print("E-Mail already exists.")
        return make_response("E-Mail already exists .",619)  
#    except ValidationError as ve:
#        return make_response("Password must be between 8-12 characters",123)


if __name__ == '__main__':
    app.run(debug=True, port=69)