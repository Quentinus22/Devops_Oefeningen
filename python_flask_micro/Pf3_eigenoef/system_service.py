from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Pf3: Microservice Experiment</h1><p>Status: Actief op poort 9000</p>"

@app.route("/status")
def status():
    return jsonify({
        "service": "Pf3-Microservice",
        "container_id": "Geen (Bare Metal)",
        "locatie": os.getcwd()
    })

if __name__ == "__main__":
    # threaded=False is essentieel voor jouw VM om crashes te voorkomen
    app.run(host="0.0.0.0", port=9000, threaded=False)