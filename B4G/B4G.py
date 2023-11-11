from flask import Flask, request
from functools import reduce

app = Flask(__name__)

# Beispiel-Daten
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@app.route('/transformiere_liste', methods=['POST'])
def transformiere_liste_route():
    if 'operation' in request.form:
        operation = request.form['operation']

        # Je nach Operation die entsprechende Funktion anwenden
        if operation == 'verdopple':
            transformierte_zahlen = list(map(lambda x: x * 2, zahlen))
        elif operation == 'waehle_gerade_aus':
            transformierte_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))
        elif operation == 'berechne_summe':
            transformierte_zahlen = reduce(lambda x, y: x + y, zahlen)
        else:
            transformierte_zahlen = []

        return {"transformierte_daten": transformierte_zahlen}

if __name__ == '__main__':
    app.run(debug=True)
