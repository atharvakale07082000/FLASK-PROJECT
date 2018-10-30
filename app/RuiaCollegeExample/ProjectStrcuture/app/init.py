from flask import Flask
from flask_bootstrap import Bootstrap


#Initialize the app
app = Flask(__name__)
bootstrap = Bootstrap(app)

import app.views



app.config.from_object('config')
