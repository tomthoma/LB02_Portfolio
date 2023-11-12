from flask import Flask, request

app = Flask(__name__)

# Lambda-Ausdruck für die Quadrierung
quadriere = lambda x: x**2

# Lambda-Ausdruck für die Konvertierung in Großbuchstaben
grossbuchstaben = lambda text: text.upper()

@app.route('/transformiere', methods=['POST'])
def transformiere_route():
    if 'operation' in request.form and 'wert' in request.form:
        operation = request.form['operation']
        wert = int(request.form['wert'])

        # Je nach Operation den entsprechenden Lambda-Ausdruck verwenden
        if operation == 'quadriere':
            ergebnis = quadriere(wert)
        elif operation == 'grossbuchstaben':
            ergebnis = grossbuchstaben(str(wert))
        else:
            ergebnis = "Ungültige Operation."

        return f"Ergebnis der Operation: {ergebnis}"

if __name__ == '__main__':
    app.run(debug=True)
