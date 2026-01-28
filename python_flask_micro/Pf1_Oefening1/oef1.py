from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Pf1:Oef1 : In orde !</h1><p>Deze oefening draait op poort 5055.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055)
