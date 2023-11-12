from flask import Flask, request

app = Flask(__name__)

def berechne_durchschnitt(zahlen):
    summe = sum(zahlen)
    anzahl = len(zahlen)
    if anzahl == 0:
        return 0
    else:
        durchschnitt = summe / anzahl
        return durchschnitt

@app.route('/durchschnitt', methods=['POST'])
def durchschnitt_route():
    if 'zahlen' in request.form:
        zahlen = list(map(float, request.form['zahlen'].split(',')))
        durchschnitt = berechne_durchschnitt(zahlen)
        return f"Durchschnitt: {durchschnitt}"

if __name__ == '__main__':
    app.run(debug=True)
