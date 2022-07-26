from operator import index
from flask import Flask, render_template, request,make_response
from flask import jsonify, redirect,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect,disconnect
from mongoengine import Document, StringField, EmailField


connect(db='DemonCyborg',host='127.0.0.1', port=27017)
print("Connected to MongoDB Database.")



class bookshelf(Document):
   book_id= StringField()
   name= StringField()
   author= StringField()
   
   def to_json(self):
       #converts this document to JSON
       return{
           "book_id":self.book_id,
           "name":self.name,
           "author":self.author
       }
app=Flask(__name__)


@app.route('/api/db_populate',methods=['POST'])
def db_populate():
   book1=bookshelf(book_id=1,name='Game of Thrones',author='George RR Martin')
   book2=bookshelf(book_id=2,name='Lord of the Rings',author='JRR Tolkien')
   book1.save()
   book2.save()
   return make_response("Books Added.",201)


@app.route("/yo", methods=["GET"]) 
def home():
    return "X"

if __name__ == '__main__':
    app.run(debug=True, port=6000)