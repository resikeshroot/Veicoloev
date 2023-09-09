from flask import *
# from user import user
from user1 import user1
from database import *

app=Flask(__name__)

# app.register_blueprint(user)
app.register_blueprint(user1)


app.run(debug=True)