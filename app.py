from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.jinja')

@app.route("/style/")
def style():
    return render_template('style.jinja')

@app.route("/minecraft/")
def minecraft():
    return render_template('minecraft.jinja')

