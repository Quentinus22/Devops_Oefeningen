from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Een simpele berekening om te laten zien dat het werkt
    getal1 = 10
    getal2 = 5
    totaal = getal1 + getal2
    return f"<h1>Examen Oefening J3</h1><p>Berekening: {getal1} + {getal2} = {totaal}</p><p>Status: Online</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6060, threaded=False)