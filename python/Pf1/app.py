from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Pf1 werkt!"

# De fout zat hieronder: het moeten 2 streepjes zijn!
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)