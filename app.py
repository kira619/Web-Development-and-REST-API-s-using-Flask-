from operator import index
from flask import Flask, render_template, request
from flask import jsonify, redirect,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect,disconnect
from mongoengine import Document, StringField, EmailField
from mongoengine.errors import NotUniqueError

app=Flask(__name__)


connect(db='DemonCyborg',host='127.0.0.1', port=27017)

print("Connected to MongoDB Database.")

class User(Document):
    email=EmailField(required= True, unique=True)
    first_name=StringField(max_length=50)
    last_name=StringField(max_length=50)
    emp_id=StringField(max_length=50)


employees = []

@app.route('/') 
def home():
    return render_template('home.html')


@app.route("/admin")
def yoyo():
    return redirect(url_for("user", name='Redirected Admin'))

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum=0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit=n%10
        sum += digit **order
        n= n//10
    if(sum == copy_n):
        print(f"{copy_n}is an Armstrong Number")
        result = {
            "Number" : copy_n,
            "ARMSTRONG" : True,
            "Server IP" : "128.234.234.213.53"
        }
    else:
        print(f"{copy_n}is not an Armstrong Number")
        result = {
            "Number" : copy_n,
            "ARMSTRONG" : False,
            "Server IP" : "128.234.234.213.54"
        }
    return jsonify(result)
    



@app.route("/goo")
def goo():
    return render_template("qwert.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["POST"])
def form():
    try:
        user = User(email = request.form.get("email"))
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.emp_id = request.form.get("emp_id")
        user.save()
    except NotUniqueError as nue:
        print("E-Mail already exists.")
        return render_template("form2.html")




    print("Data succesfully Uplaoded to MongoDB Database.")
    #employees.append(f"{emp_id} | {first_name} {last_name} | {email}")
    print('Data Uploaded!')
    return render_template("form.html",employees=employees)




if __name__ == '__main__':
    app.run(debug=True, port=619)