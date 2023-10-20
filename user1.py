from flask import *
from database import *


user1=Blueprint('user1',__name__)


@user1.route("/")
def fpage():
    return render_template("home.html")

@user1.route("/login",methods=['get','post'])
def logpage():

    if "sub" in request.form:
        username=request.form['username']
        pwd=request.form['password']

        print(username,pwd)


    return render_template("Login.html")

@user1.route("/register",methods=['get','post'])
def regpage():
    if "login" in request.form:
        Firstname=request.form['fname']
        Lastname=request.form['lname']
        email=request.form['email']
        Phonenumber=request.form['phn']
        Age=request.form['Age']
        Dob=request.form['dob']
        username=request.form['uname']
        pwd=request.form['psw']

        K="INSERT INTO login VALUES(null,'user','%s','%s')"%(username,pwd)

        lid=insert(K)

        d="insert into register values('%s','%s','%s','%s','%s','%s','%s',null)"%(Firstname,Lastname,email,Phonenumber,Age,Dob,lid)

        insert(d)


    return render_template("register.html"))
