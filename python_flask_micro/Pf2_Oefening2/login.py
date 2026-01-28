from flask import Flask, render_template, request

app = Flask(__name__)

# We veranderen de logica naar een 'Portaal' toegang
@app.route("/", methods=["GET", "POST"])
def portaal_toegang():
    foutmelding = None
    if request.method == "POST":
        gebruiker = request.form.get('user_id')
        wachtwoord = request.form.get('secret_key')

        # Nieuwe unieke inloggegevens
        if gebruiker == 'examen_user' and wachtwoord == 'DevNet2026':
            return "<h2>Systeem Status: Geautoriseerd</h2><p>Welkom bij het Pf2 Dashboard.</p>"
        else:
            foutmelding = "Toegang geweigerd: Ongeldige ID of Sleutel."

    return render_template("index.html", error=foutmelding)

if __name__ == "__main__":
    # threaded=False is essentieel voor jouw VM omgeving
    app.run(host="0.0.0.0", port=5056, threaded=False)