from flask import Flask, request

app = Flask(__name__)

# Vor dem Refactoring
@app.route('/quadratzahlen_bis_n/<int:n>', methods=['GET'])
def quadratzahlen_bis_n_route(n):
    quadratzahlen = []
    for i in range(1, n+1):
        quadratzahlen.append(i**2)
    return {"quadratzahlen": quadratzahlen}

# Nach dem Refactoring
@app.route('/quadratzahlen_bis_n_refactored/<int:n>', methods=['GET'])
def quadratzahlen_bis_n_refactored_route(n):
    quadratzahlen = [i**2 for i in range(1, n+1)]
    return {"quadratzahlen": quadratzahlen}

if __name__ == '__main__':
    app.run(debug=True)
