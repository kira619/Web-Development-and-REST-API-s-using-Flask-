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


def validate_password3(password):
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
    

#    if not result:
#        raise Exception('Please include some special Characters')

print(validate_password3("tamojit@ark"))