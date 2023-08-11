from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import g
from flask import flash

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms.validators import InputRequired

from .models import db
from .models import Article
from .models import User

import os


@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")


@flask_app.route("/about/")
def view_about():
    return render_template("about.jinja")
