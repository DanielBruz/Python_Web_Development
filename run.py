from mdblog.app import flask_app

# kdyz je tento program run.py spusteny jako hlavni, nastavi se promenna __name__ na __main__.
# Kdybych tento program importoval jako modul v jiném programu, nastavila by se na "run".
# Níže je uvedena IP adresa mé virtuální linux mašiny 192.168.20.165 (v práci). Doma = 10.0.0.196

if __name__ == "__main__":
    debug = True
    host = "10.0.0.196"
    flask_app.run(host, debug=debug)
