from flask import Flask, request

app = Flask(__name__)

def quadriere(zahl):
    return zahl ** 2

def kubiere(zahl):
    return zahl ** 3

def transformiere_liste(funktion, liste):
    return [funktion(zahl) for zahl in liste]

@app.route('/transformiere', methods=['POST'])
def transformiere_route():
    if 'operation' in request.form and 'zahlen' in request.form:
        operation = request.form['operation']
        zahlen = list(map(int, request.form['zahlen'].split(',')))

        # Funktion je nach Operation auswählen
        if operation == 'quadriere':
            transformierte_zahlen = transformiere_liste(quadriere, zahlen)
        elif operation == 'kubiere':
            transformierte_zahlen = transformiere_liste(kubiere, zahlen)
        else:
            transformierte_zahlen = []

        return f"Transformierte Zahlen: {transformierte_zahlen}"

if __name__ == '__main__':
    app.run(debug=True)
