from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_bcrypt import Bcrypt

Bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


