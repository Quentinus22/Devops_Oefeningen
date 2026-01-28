from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Dit is de HTML voor je formulier, we zetten het even in een variabele voor het gemak
HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Ap4 - API Experiment 2</title>
    <style>
        body { font-family: sans-serif; margin: 40px; line-height: 1.6; }
        .container { max-width: 500px; background: #f4f4f4; padding: 20px; border-radius: 8px; }
        input { display: block; width: 100%; margin-bottom: 10px; padding: 8px; }
        button { background: #007bff; color: white; border: none; padding: 10px; cursor: pointer; width: 100%; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Ap4: API Webformulier</h2>
        <form method="POST" action="/api/verwerk">
            <label>Gebruikersnaam:</label>
            <input type="text" name="username" placeholder="Typ je naam..." required>
            
            <label>Bericht:</label>
            <input type="text" name="message" placeholder="Typ een bericht..." required>
            
            <button type="submit">Verstuur naar API</button>
        </form>
    </div>
</body>
</html>
'''

# Route 1: Toon het webformulier (GET)
@app.route('/')
def index():
    return render_template_string(HTML_FORM)

# Route 2: De API-endpoint die de data verwerkt (POST)
@app.route('/api/verwerk', methods=['POST'])
def verwerk_data():
    # We halen de data uit het formulier (webform parsing)
    naam = request.form.get('username')
    bericht = request.form.get('message')
    
    # We sturen een JSON response terug (typisch voor een API)
    return jsonify({
        "status": "success",
        "ontvangen_naam": naam,
        "ontvangen_bericht": bericht,
        "server_tijd": "2026-01-28" 
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)