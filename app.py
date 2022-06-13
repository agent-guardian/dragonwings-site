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

@app.errorhandler(400)
def bad_request(e):
    return render_template('400.jinja'), 400

@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.jinja'), 401

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.jinja'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.jinja'), 404

