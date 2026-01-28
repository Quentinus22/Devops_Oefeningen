from flask import Flask, render_template
from datetime import datetime

# We noemen de app anders
examen_app = Flask(__name__)

@examen_app.route("/")
def home():
    # We geven de huidige tijd mee naar de pagina
    nu = datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", tijd=nu)

if __name__ == "__main__":
    examen_app.run(host='0.0.0.0', port=7000, threaded=False)