from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "J1_jenkins: In orde!"

if __name__ == "__main__":
    # Zet threading UIT om crashes te voorkomen
    app.run(host="0.0.0.0", port=5050, threaded=False)
