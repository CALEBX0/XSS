from flask import Flask, request, render_template, redirect, make_response
import sqlite3

app = Flask(__name__)
DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    # === Entrada desde URL GET ===
    mensaje_url = request.args.get("q", "")

    # === Entrada desde Cookie ===
    cookie_msg = request.cookies.get("mensaje_cookie", "")

    # === Entrada desde cabecera ===
    user_agent = request.headers.get("User-Agent", "")

    # === Entrada desde formulario POST ===
    mensaje_post = ""
    if request.method == "POST":
        mensaje_post = request.form.get("texto", "")
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO mensajes (texto) VALUES (?)", (mensaje_post,))
        conn.commit()
        conn.close()
        return redirect("/")

    # === Leer mensajes almacenados ===
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT texto FROM mensajes")
    mensajes = c.fetchall()
    conn.close()

    # === Preparar respuesta y setear cookie ===
    resp = make_response(render_template("index.html", 
        mensajes=mensajes,
        mensaje_url=mensaje_url,
        cookie_msg=cookie_msg,
        user_agent=user_agent
    ))

    if mensaje_url:
        resp.set_cookie("mensaje_cookie", mensaje_url)

    return resp

# === Ruta dinámica vulnerable ===
@app.route("/perfil/<nombre>")
def perfil(nombre):
    return f"<h1>Perfil del usuario: {nombre}</h1>"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)


