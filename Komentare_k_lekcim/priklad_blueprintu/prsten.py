from flask import Blueprint

formicka_na_prsten = Blueprint("formicka_na_prsten", __name__)  # dáme mu jako argument jen jméno tohoto modulu


@formicka_na_prsten.route("/velikost/")
def velikost():
    return "to je velikost prstenu"


@formicka_na_prsten.route("/gravirovani/")
def gravirovani():
    return "to je gravirovani prstenu"
