from operator import index
from flask import Flask, render_template, request
from flask import jsonify, redirect,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect,disconnect
from mongoengine import Document, StringField, EmailField
connect(db='DemonCyborg',host='127.0.0.1', port=27017)

print("Connected to MongoDB Database.")

class bookshelf(Document):
    book_id=StringField(max_length=50)
    author=StringField(max_length=50)
    book_name=StringField(max_length=50)

book = bookshelf(book_id='1')
book.author='Tamojit'
book.book_name='book1'
book.save()
print("Data succesfully Uplaoded to MongoDB Database.")
