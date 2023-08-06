from mdblog.app import flask_app
from mdblog.app import init_db

import sys


# kdyz je tento program run.py spusteny jako hlavni, nastavi se promenna __name__ na __main__.
# Kdybych tento program importoval jako modul v jiném programu, nastavila by se na "run".
# Níže je uvedena IP adresa mé virtuální linux mašiny 192.168.20.165 (v práci). Doma = 10.0.0.196

def start():
    debug = True
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)


def init():
    init_db(flask_app)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        commad = sys.argv[1]
        if commad == "start":
            start()
        elif commad == "init":
            init()
    else:
        print("usage:\n\n\trun.py [ start | init ]")
