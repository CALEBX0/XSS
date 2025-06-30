from flask import Flask, request, render_template, redirect
import sqlite3
# import bleach 
app = Flask(__name__)
DB = "Hackmazon.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # Tabla para comentarios (producto, texto)
    c.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            texto TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# def TextoSeguro(texto):
#     return bleach.clean(texto, tags=[], attributes={}, strip=True)



 # Política CSP muy restrictiva: solo scripts de la misma fuente
# @app.after_request
# def set_csp(response):
   
#     csp = "default-src 'self'; script-src 'self'; style-src 'self' https://cdn.jsdelivr.net; object-src 'none';"
#     response.headers['Content-Security-Policy'] = csp
#     return response



@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    if request.method == "POST":
        # Guardar comentario
        producto = request.form.get("producto")
        texto = request.form.get("comentario")
        if producto and texto:
            # texto = TextoSeguro(texto)
            c.execute("INSERT INTO comentarios (producto, texto) VALUES (?, ?)", (producto, texto ))
            conn.commit()
        return redirect("/")

    # Leer comentarios por producto
    c.execute("SELECT producto, texto FROM comentarios")
    rows = c.fetchall()

    comentarios_por_producto = {}
    for prod, texto in rows:
        comentarios_por_producto.setdefault(prod, []).append(texto)

    conn.close()

    productos = [
        {
            "id": "ps4",
            "nombre": "Dual Shock PS4",
            "descripcion": "Control para jugar en la PlayStation 4 con alta precisión.",
            "precio": "200.00 MXN",
            "imagen": "/static/img/aa.jpg"
        },
        {
            "id": "labubu",
            "nombre": "Labubu",
            "descripcion": "El llavero más tierno del mundo para acompañarte siempre.",
            "precio": "49.00 MXN",
            "imagen": "/static/img/Labubu.jpeg"
        },
        {
            "id": "macbook",
            "nombre": "MacBook Pro 14\"",
            "descripcion": "Potente portátil con 16GB de RAM unificada y SSD de 512GB.",
            "precio": "3,299.00 MXN",
            "imagen": "/static/img/mc.jpeg"
        }
    ]

    return render_template("hackmazon.html", productos=productos, comentarios=comentarios_por_producto)


if __name__ == "__main__":
    init_db()
    app.run(debug=True,port=8912)
