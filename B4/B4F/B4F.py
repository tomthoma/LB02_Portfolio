from flask import Flask, request
from functools import reduce

app = Flask(__name__)

# Beispiel-Daten
studenten = [
    {"name": "Alice", "alter": 22, "noten": [80, 85, 90]},
    {"name": "Bob", "alter": 19, "noten": [75, 88, 92]},
    {"name": "Charlie", "alter": 25, "noten": [90, 92, 95]},
    {"name": "David", "alter": 21, "noten": [78, 85, 88]},
]

@app.route('/berechne_durchschnittsnote_aelter_20', methods=['GET'])
def berechne_durchschnittsnote_route():
    # Kombinierte Anwendung von map, filter und reduce
    durchschnittsnote = reduce(
        lambda x, y: x + y,
        map(lambda student: sum(student["noten"]), filter(lambda student: student["alter"] > 20, studenten)),
    ) / len(studenten)

    return {"durchschnittsnote_aelter_20": durchschnittsnote}

if __name__ == '__main__':
    app.run(debug=True)
