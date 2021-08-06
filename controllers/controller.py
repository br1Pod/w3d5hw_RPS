from flask import request, render_template
from app import app
from models.game import *
from models.player import *

@app.route("/")
def index():
    return render_template("index.html", title="Home")