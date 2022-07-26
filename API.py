from operator import index
from flask import Flask, render_template, request,make_response
from flask import jsonify, redirect,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect,disconnect
from mongoengine import Document, StringField, EmailField
from mongoengine.errors import NotUniqueError


app=Flask(__name__)

connect(db='DemonCyborg',host='127.0.0.1', port=27017)

print("Connected to MongoDB Database.")



class bookshelf(Document):
    book_id=StringField(max_length=50)
    author=StringField(max_length=50)
    book_name=StringField(max_length=50)
    def to_json(self):
       #converts this document to JSON
       return{
           "book_id":self.book_id,
           "author":self.author,
           "book_name":self.book_name,

       }




@app.route("/goo")
def goo():
    return render_template("qwert.html")

@app.route('/api/db_populate',methods=['POST'])
def db_populate():
    book = bookshelf(book_id='1')
    book.author='George RR Martin'
    book.book_name='Game of Thrones'
    book2=bookshelf(book_id='2',book_name='Lord of the Rings',author='JRR Tolkien')
    book.save()
    book2.save()
    return make_response("Books Added.",619)


@app.route('/api/books',methods=['GET','POST'])
def api_books():
   if request.method ==  "GET":
        mylist=[]     
        for book in bookshelf.objects():
            mylist.append(book.to_json())
            print(mylist)
        return make_response(jsonify(mylist),200)          

   elif request.method == "POST":
        content = request.json
        book3= bookshelf(book_id=content['book_id'],author=content['author'],book_name=content['book_name'])
        book3.save()
        return make_response("Books Added",201)





if __name__ == '__main__':
    app.run(debug=True, port=619)