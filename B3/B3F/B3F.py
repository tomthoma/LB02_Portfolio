from flask import Flask, request

app = Flask(__name__)

# Lambda-Ausdruck für die Multiplikation zweier Zahlen
multipliziere = lambda x, y: x * y

# Lambda-Ausdruck für die Verkettung von zwei Strings mit einem Trennzeichen
verkette_mit_trennzeichen = lambda str1, str2, trennzeichen: str1 + trennzeichen + str2

@app.route('/transformiere', methods=['POST'])
def transformiere_route():
    if 'operation' in request.form and 'wert1' in request.form and 'wert2' in request.form:
        operation = request.form['operation']
        wert1 = int(request.form['wert1'])
        wert2 = int(request.form['wert2'])

        # Je nach Operation den entsprechenden Lambda-Ausdruck verwenden
        if operation == 'multipliziere':
            ergebnis = multipliziere(wert1, wert2)
        elif operation == 'verkette_mit_trennzeichen':
            trennzeichen = request.form.get('trennzeichen', '')
            ergebnis = verkette_mit_trennzeichen(str(wert1), str(wert2), trennzeichen)
        else:
            ergebnis = "Ungültige Operation."

        return f"Ergebnis der Operation: {ergebnis}"

if __name__ == '__main__':
    app.run(debug=True)
