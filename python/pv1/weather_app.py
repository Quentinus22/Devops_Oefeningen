from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Onze "Database"
WEATHER_DB = {
    "brussel": {"temp": "12°C", "status": "Bewolkt"},
    "antwerpen": {"temp": "14°C", "status": "Zonnig"},
    "gent": {"temp": "11°C", "status": "Lichte regen"}
}

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Weather API</title></head>
<body style="font-family:sans-serif; text-align:center; padding-top:50px;">
    <h2>Voer een stad in voor de API:</h2>
    <form method="POST" action="/get_weather">
        <input type="text" name="city" placeholder="Stad..." required>
        <button type="submit">Vraag Weer op</button>
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # De 'Webform' data ophalen
    stad = request.form.get('city').lower()
    
    if stad in WEATHER_DB:
        data = WEATHER_DB[stad]
        return jsonify({
            "status": "success",
            "stad": stad.capitalize(),
            "weer": data
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Stad niet gevonden in API database"
        }), 404

if __name__ == '__main__':
    app.run(debug=True)