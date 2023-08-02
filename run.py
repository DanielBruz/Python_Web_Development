from app import flask_app

if __name__ == "__main__":
    debug = False
    host = "192.168.20.165"
    flask_app.run(host, debug=debug)

