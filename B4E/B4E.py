from flask import Flask, request
from functools import reduce

app = Flask(__name__)

# Beispiel-Daten
bestellungen = [
    {"kunde": "Alice", "produkt": "Apfel", "menge": 5},
    {"kunde": "Bob", "produkt": "Banane", "menge": 3},
    {"kunde": "Charlie", "produkt": "Apfel", "menge": 2},
    {"kunde": "David", "produkt": "Orange", "menge": 4},
    {"kunde": "Alice", "produkt": "Banane", "menge": 6},
]

@app.route('/gesamtmenge_produkt', methods=['GET'])
def gesamtmenge_produkt_route():
    if 'produkt' in request.args:
        produkt = request.args['produkt']

        # Aggregation mit map, filter und reduce
        gesamtmenge = reduce(
            lambda x, y: x + y,
            map(lambda bestellung: bestellung["menge"], filter(lambda bestellung: bestellung["produkt"] == produkt, bestellungen)),
        )

        return {"gesamtmenge": gesamtmenge}

if __name__ == '__main__':
    app.run(debug=True)
