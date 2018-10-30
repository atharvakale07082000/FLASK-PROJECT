from flask import Flask
from flask_bootstrap import Bootstrap


#Initialize the app
app = Flask(__name__)
bootstrap = Bootstrap(app)
#Load the views
from app import views



app.config.from_object('config')
