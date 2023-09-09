from flask import *
from database import *


user=Blueprint('user',__name__)


@user.route("/")
def fpage():
    return render_template("home.html")

@user.route("/login",methods=['get','post'])
def logpage():

    if "sub" in request.form:
        username=request.form['username']
        pwd=request.form['password']

        print(username,pwd)


    return render_template("Login.html")

@user.route("/register")
def regpage():
    # if "login" in request.form:
    #     Firstname=request.form['username']
    #     Lastname=request.form['username']
    #     email=request.form['username']
    #     Phonenumber=request.form['username']
    #     Age=request.form['username']
    #     Dob=request.form['username']
    #     username=request.form['secname']
    #     pwd=request.form['psw']
    #     print(username,pwd)
    return render_template("register.html")



