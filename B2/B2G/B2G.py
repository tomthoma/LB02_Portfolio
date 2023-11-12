from flask import Flask, request

app = Flask(__name__)

def gruss(name):
    return f"Hallo, {name}!"

def abschied(name):
    return f"Auf Wiedersehen, {name}!"

def rufe_begrussung_funktion_auf(func, name):
    return func(name)

@app.route('/begruessung', methods=['POST'])
def begruessung_route():
    if 'art' in request.form and 'name' in request.form:
        art_der_begrussung = request.form['art']
        name = request.form['name']

        # Funktion je nach Art auswählen
        if art_der_begrussung == 'gruss':
            ausgabe = rufe_begrussung_funktion_auf(gruss, name)
        elif art_der_begrussung == 'abschied':
            ausgabe = rufe_begrussung_funktion_auf(abschied, name)
        else:
            ausgabe = "Ungültige Art der Begrüßung."

        return ausgabe

if __name__ == '__main__':
    app.run(debug=True)
