from flask import Flask

import os

flask_app = Flask(__name__)
flask_app.config.from_pyfile("/vagrant/configs/default.py")
flask_app.config.from_pyfile("/vagrant/configs/development.py")
if "MDBLOG_CONFIG" in os.environ:
    flask_app.config.from_envvar("MDBLOG_CONFIG")

db.init_app(flask_app)

## CLI COMMAND
def init_db(app):
    with app.app_context():
        db.create_all()
        print("database inicialized")

        default_user = User(username="admin")
        default_user.set_password("admin")

        db.session.add(default_user)
        db.session.commit()
        print("default user was created")

