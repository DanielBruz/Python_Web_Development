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


@flask_app.route("/articles/", methods=["GET"])
def view_articles():
    articles = Article.query.order_by(Article.id.desc())
    return render_template("articles.jinja", articles=articles)


@flask_app.route("/articles/<int:art_id>/")
def view_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        return render_template("article.jinja", article=article)
    return render_template("article_not_found.jinja", art_id=art_id)
