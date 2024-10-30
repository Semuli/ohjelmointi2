from flask import Flask, Response
import math
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        juokseva_luku = 0
        i = 2

        while i < math.sqrt(int(luku)):
            if int(luku) % i == 0:
                juokseva_luku += 1
            i += 1

        if juokseva_luku != 0:
            isprime = False
        else:
            isprime = True

        vastaus = {
            "Number" : luku,
            "isPrime" : isprime
        }
        return vastaus

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku. Annakokonaisluku"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)