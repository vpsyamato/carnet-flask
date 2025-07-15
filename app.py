from flask import Flask, render_template, request, redirect
from db import ajouter_contact, lister_contacts, get_contact, modifier_contact, supprimer_contact
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    contacts = lister_contacts()
    return render_template("index.html", contacts=contacts)

@app.route("/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        nom = request.form["nom"]
        numero = request.form["numero"]
        if nom and numero:
            ajouter_contact(nom, numero)
        return redirect("/")
    return render_template("ajouter.html")

@app.route("/modifier/<int:id>", methods=["GET", "POST"])
def modifier(id):
    contact = get_contact(id)
    if request.method == "POST":
        nom = request.form["nom"]
        numero = request.form["numero"]
        modifier_contact(id, nom, numero)
        return redirect("/")
    return render_template("modifier.html", contact=contact)

@app.route("/supprimer/<int:id>")
def supprimer(id):
    supprimer_contact(id)
    return redirect("/")

# ✅ GESTIONNAIRE D'ERREUR 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

# ✅ TOUJOURS À LA FIN
if __name__ == "__main__":
    app.run(debug=False)
