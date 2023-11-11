from flask import Flask, jsonify

app = Flask(__name__)

# Beispiel einer pure function
def add(x, y):
    return x + y

# Route für die Anwendung der pure function
@app.route('/')
def home():
    # Anwendung der pure function
    result = add(3, 5)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

