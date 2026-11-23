
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data menu sementara
menus = [
    {"id": 1, "nama": "Nasi Goreng", "kategori": "Makanan",
     "harga": 15000, "stok": 20},
    {"id": 2, "nama": "Ayam Geprek", "kategori": "Makanan",
     "harga": 18000, "stok": 15},
    {"id": 3, "nama": "Es Teh", "kategori": "Minuman",
     "harga": 5000, "stok": 30},
    {"id": 4, "nama": "Mie Goreng", "kategori": "Makanan",
     "harga": 12000, "stok": 10}
]

@app.route("/")
def index():
    total_menu = len(menus)
    total_stok = sum(menu["stok"] for menu in menus)
    total_makanan = len([
        menu for menu in menus
        if menu["kategori"] == "Makanan"
    ])

    rekomendasi = [
        menu for menu in menus if menu["stok"] > 0
    ]

    return render_template(
        "index.html",
        menus=menus,
        total_menu=total_menu,
        total_stok=total_stok,
        total_makanan=total_makanan,
        rekomendasi=rekomendasi
    )

@app.route("/tambah", methods=["POST"])
def tambah():
    nama = request.form["nama"]
    kategori = request.form["kategori"]
    harga = int(request.form["harga"])
    stok = int(request.form["stok"])

    menu_baru = {
        "id": max([m["id"] for m in menus], default=0) + 1,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }

    menus.append(menu_baru)
    return redirect(url_for("index"))

@app.route("/hapus/<int:id>")
def hapus(id):
    global menus
    menus = [menu for menu in menus if menu["id"] != id]
    return redirect(url_for("index"))

@app.route("/stok/<int:id>", methods=["POST"])
def update_stok(id):
    for menu in menus:
        if menu["id"] == id:
            menu["stok"] = max(0, int(request.form["stok"]))
            break

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
