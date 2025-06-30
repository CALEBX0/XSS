from flask import Flask, request, render_template,flash




app = Flask(__name__)
app.secret_key = "paquejalealert"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Procesar el formulario
        pass
    return render_template("fm.html")
@app.route("/registro", methods=["GET", "POST"])
def registro():
    flash("💀💀💀 Te acabas de regalar padrino 💀💀💀")
    return render_template("fm.html")



if __name__ == "__main__":
    app.run(debug=True ,port=8922)
