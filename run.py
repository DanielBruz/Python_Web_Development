from mdblog.app import flask_app
from mdblog.app import init_db

import sys


# kdyz je tento program run.py spusteny jako hlavni, nastavi se promenna __name__ na __main__.
# Kdybych tento program importoval jako modul v jiném programu, nastavila by se na "run".
# Níže je uvedena IP adresa mé virtuální linux mašiny 192.168.20.172 (v práci). Doma = 10.0.0.196. 158 je linux doma.

def start():
    debug = True
    host = "192.168.20.161"
    flask_app.run(host, debug=debug)


def init():
    init_db(flask_app)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "start":
            start()
        elif command == "init":
            init()
    else:
        print("usage:\n\n\trun.py [ start | init ]")
