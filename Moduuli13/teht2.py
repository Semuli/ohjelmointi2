from flask import Flask, Response
import mysql.connector
import json

connection = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database= 'flight_game',
    user= 'mikko',
    password= 'salasana',
    autocommit=True
    )

app = Flask(__name__)
@app.route('/kentta/<icao>')

def get_airport_by_icao(icao):
    try:
        sql = f'SELECT name, municipality FROM airport Where ident = "{icao}"'
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        airport_data = cursor.fetchall()
        tilakoodi = 200
        if airport_data == []:
            vastaus = {
                "ICAO" : icao,
                "teksi" : "Virheellinen ICAO-koodi"
            }
        else:
            vastaus = {
                "ICAO": icao,
                "Name": airport_data[0]["name"],
                "Municipality": airport_data[0]["municipality"]
            }

    except ValueError:
        tilakoodi = 500
        vastaus = {
            "status" : tilakoodi,
            "teksti" : "Virheellinen ICAO-koodi"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen reitti"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)