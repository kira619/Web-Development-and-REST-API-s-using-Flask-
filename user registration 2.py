from operator import index
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import jsonify
from flask import redirect
from flask import url_for

from mongoengine import connect
from mongoengine import Document
from mongoengine import StringField
from mongoengine import EmailField
from mongoengine import IntField
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError

import re

# Init Flask Server
app=Flask(__name__)

# Connect to DB
connect(db='DemonCyborg',
        host='127.0.0.1',
        port=27017,
        )

print("Connected to MongoDB Database.")

# Mongo Engine Model 
class UserDetails(Document):
    full_name = StringField(max_length=50)
    email = EmailField(required= True, unique=True)
    mobile_no = IntField(max_length=50)
    password = StringField(required= True,min_length=8,max_length=12)
    confirm_password  = StringField(max_length=50)
    gender = StringField(max_length=50)


    def to_json(self):
       return{
           "full_name":self.full_name,
           "email":self.email,
           "mobile_no":self.mobile_no,
           "password":self.password,
           "confirm_password":self.confirm_password,
           "gender":self.gender,
       }


# Common Functions
# =======================
def validate_gender(gender):
    """
    validates gender (male,female,others)
    """
    genders = ['Male','Female','Others']
    if gender in genders:
        pass

    else:
        raise Exception(f'Please select from {genders} in gender.')



def validate_password(password):
    """
    validate password format and length
    """
    if len(password) <= 8 or len(password) >= 12  :
        raise Exception('Password must be between 8-12 characters')
    c=0
    x = password
    s='[@_!#$%^&*()<>?/\|}{~:]' # special character set
    for i in range(len(x)):
    # checking if any special character is present in given string or not
        if x[i] in s:
            c+=1   # if special character found then add 1 to the c
        else:
            pass
    if c>0:
        print(f'Password Accepted, {c} special characters found.')

    else:
        raise Exception('Password must include atleast one special character.')    

        


def validate_confirm_password(password,confirm_password):
    """
    checks if password and validate password are similar. 
    """


    if password != confirm_password :
        raise Exception('password and confirm_password must be similar.')


    else:
        pass


def validate_email(email):
    """
    validate email format and
    check if already exists
    TODO raise exceptions same as password validation
    """
    
    # check in UserDetails of email already exists
    user = UserDetails.objects(email=email)
    if user:
        raise Exception(f'User with this {email} email already exists')




    # check if valid email format
@app.route('/populate',methods=['POST'])
def db_populate():
    book = UserDetails(full_name='Tamojit Sarkar')
    book.email='tamojitsarkar619@gmail.com'
    book.mobile_no='9891052574'
    book.password='Welcome@123'
    book.confirm_password='Welcome@123'
    book.gender='Alpha Male'
    book.save()
    return make_response("USER Added.",619)


# API to get users list
@app.route('/show-users',methods=['GET'])
def show_users():
   if request.method ==  "GET":
        mylist=[]     
        for x in UserDetails.objects():
            mylist.append(x.to_json())
        return make_response(jsonify(mylist),200)    

# API to register new users
@app.route('/add-users',methods=['POST'])
def add_users():
    if request.method == "POST":
        content = request.json
        try:
            # Call Validations
            validate_email(content['email'])
            validate_password(content['password'])
            validate_confirm_password(content['password'],content['confirm_password'])
            validate_gender(content['gender'])

            user_details = UserDetails(full_name=content['full_name'],
                                email=content['email'],
                                mobile_no=content['mobile_no'],
                                password=content['password'],
                                confirm_password=content['confirm_password'],
                                gender=content['gender'],
                                )
            user_details.save()

            return make_response("User Succesfully Added", 200)

        except Exception as ex:
            return make_response(repr(ex), 500)

# main function to run server
if __name__ == '__main__':
    app.run(debug=True, port=69)