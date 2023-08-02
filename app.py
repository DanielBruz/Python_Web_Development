from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/")  # URL adresa, na které poběží moje funkce
def index():
    return "Hello World"
