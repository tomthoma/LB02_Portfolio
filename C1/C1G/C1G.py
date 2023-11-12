from flask import Flask, request

app = Flask(__name__)

# Vor dem Refactoring
@app.route('/verarbeite_daten', methods=['POST'])
def verarbeite_daten():
    data = request.get_json()
    result = process_data(data)
    return {"result": result}

def process_data(data):
    # Lange Logik hier...
    return "processed_result"

# Nach dem Refactoring
@app.route('/verarbeite_daten_refactored', methods=['POST'])
def verarbeite_daten_refactored():
    data = request.get_json()
    result = process_data_refactored(data)
    return {"result": result}

def process_data_refactored(data):
    # Kürzere Logik hier...
    return "processed_result_refactored"

if __name__ == '__main__':
    app.run(debug=True)
