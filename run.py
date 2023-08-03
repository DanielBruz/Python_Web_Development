from app import flask_app

# kdyz je tento program run.py spusteny jako hlavni, nastavi se promenna __name__ na __main__.
# Kdybych tento program importoval jako modul v jiném programu, nastavila by se na "run".
if __name__ == "__main__":
    debug = False
    host = "192.168.20.165"
    flask_app.run(host, debug=debug)

