from flask import Flask

app = Flask(__name__)

# Beispiel für eine Liste (mutable)
mutable_list = [1, 2, 3]

# Beispiel für ein Tupel (immutable)
immutable_tuple = (1, 2, 3)

@app.route('/')
def index():
    return f"Mutable List: {mutable_list}<br>Immutable Tuple: {immutable_tuple}"

if __name__ == '__main__':
    app.run(debug=True)
