from urllib import request
from API import MongoDB_wrapper, Security
from flask import Flask, render_template
from pymongo import MongoClient

import json


# Just added gpg to my second laptop let see if this works[#Jacky]

# Setting up Database for the project
client = MongoClient("mongo")
mongo = MongoDB_wrapper(client)
print("mongoDB is up I think")

# Setting up the Security
security = Security()
print("Security is setup I think")

# Setting up the App
app = Flask("blue_Jesse")
print("App running I think")


@app.route("/") # converts normal function to view function
def homepage(): # view function
    print("Someone is at the homepage", flush=True)
    return render_template("index.html")

    '''
    When calling render_templates it search for the html files in the template folder
    you can pass in a key value pair to override the value at the localtion of the html template example:
    ----html----
    e.g. {{test}}
    ----html----
    render_template(html, test=5) [#Jacky]
    '''

@app.route("/login", methods=["GET"]) # Only get method
def loginPage():
    return render_template("login.html") # Files can be served easier with static files check flask documenation


@app.route("/loginData", methods=["POST"]) # Only post method
def logging_userData():
    forumData = request.form

    # Some how get data from the form 
    # Waiting for frontend
    username = ""
    password = ""

    if security_password_and_user_checker(username=username, password=password):
        # if the input is bad we redirect it to the login page
        return
    else:    
        # Let hash the password
        hashed_password = security.hash_265(password)
        # Structure the data input to database
        user = {"username": username, "password": hashed_password}
        # Insert the hash password
        MongoDB_wrapper.insert(user)
        # print(format) # User name should be max 12 characters
        # special characters that we don't want in username: &, ~, /, <,   >, ;, [space]
        # direct the user to the user homepage [#Jacky]

@app.route("/changelog")
def display_changelog():
    change_data = open("changelogs.txt", "r").readlines()
    # This will use the template feature of flask and use that to display a text file that I will write on the side for all the changes I made and the goals this can also be used to test
    return render_template("changelog.html", change=change_data)

# app.run() # Don't use this for final product [#Jacky]

