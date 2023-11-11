from flask import Flask, request

app = Flask(__name__)

# Liste von Benutzern mit Namen und Alter
benutzer = [
    {"name": "Alice", "alter": 30},
    {"name": "Bob", "alter": 25},
    {"name": "Charlie", "alter": 35},
    {"name": "David", "alter": 28},
]

@app.route('/sortiere_benutzer', methods=['POST'])
def sortiere_benutzer_route():
    if 'kriterium' in request.form:
        kriterium = request.form['kriterium']

        # Je nach Kriterium die Liste von Benutzern sortieren
        if kriterium == 'nach_name':
            sortierte_benutzer = sorted(benutzer, key=lambda x: x['name'])
        elif kriterium == 'nach_alter':
            sortierte_benutzer = sorted(benutzer, key=lambda x: x['alter'])
        else:
            sortierte_benutzer = benutzer

        return {"sortierte_benutzer": sortierte_benutzer}

if __name__ == '__main__':
    app.run(debug=True)
