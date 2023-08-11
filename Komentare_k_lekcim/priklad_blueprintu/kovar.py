from flask import Flask
# naimportujeme náš Blueprint:
from prsten import formicka_na_prsten

flask_app = Flask(__name__)

# vytvoříme jednotlivé instance Blueprintu; do nich otisknu svojí definici (formičku) a pověsím jí na URL:
flask_app.register_blueprint(formicka_na_prsten, url_prefix="/zlato")
flask_app.register_blueprint(formicka_na_prsten, name="blueprint_2", url_prefix="/stribro")
flask_app.register_blueprint(formicka_na_prsten, name="blueprint_3", url_prefix="/titan")

#  a spustím svou appku:
flask_app.run("10.0.0.196")
