from flask import Flask, render_template, request, jsonify
try:
    import requests
except ImportError:
    requests = None

app = Flask(__name__)

# ====================================================================
# DATA IN-MEMORY (DATABASE SEMENTARA)
# Daftar menu awal kantin kampus
# ====================================================================
menu_kantin = [
    {
        "id": 1,
        "nama": "Nasi Goreng Spesial",
        "harga": 15000,
        "kategori": "Makanan",
        "stok": 20
    },
    {
        "id": 2,
        "nama": "Mie Ayam Bakso",
        "harga": 13000,
        "kategori": "Makanan",
        "stok": 15
    },
    {
        "id": 3,
        "nama": "Es Teh Manis Jumbo",
        "harga": 5000,
        "kategori": "Minuman",
        "stok": 50
    },
    {
        "id": 4,
        "nama": "Kopi Susu Gula Aren",
        "harga": 10000,
        "kategori": "Minuman",
        "stok": 30
    }
]


# ====================================================================
# FUNGSI BANTUAN (HELPER)
# ====================================================================
def cari_menu_by_id(item_id):
    """Mencari dictionary menu berdasarkan ID, return None jika tidak ada."""
    for item in menu_kantin:
        if item["id"] == item_id:
            return item
    return None


# ====================================================================
# ROUTE VIEW: HALAMAN DASHBOARD FRONTEND
# ====================================================================
@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 1:
# Buat Endpoint GET /api/menu (Semua Menu) & /api/menu/<int:item_id> (Detail)
# ====================================================================
# TULIS KODE LANGKAH 1 (GET SEMUA & GET BY ID) DI SINI
# ====================================================================


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 2:
# Buat Endpoint POST /api/menu (Tambah Menu Baru dengan Validasi)
# ====================================================================
# TULIS KODE LANGKAH 2 (POST MENU) DI SINI
# ====================================================================


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 3:
# Buat Endpoint PUT /api/menu/<int:item_id> & DELETE /api/menu/<int:item_id>
# ====================================================================
# TULIS KODE LANGKAH 3 (PUT & DELETE) DI SINI
# ====================================================================


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 4:
# Integrasi API Eksternal: GET /api/cuaca-kampus via Open-Meteo
# ====================================================================
# TULIS KODE LANGKAH 4 (EXTERNAL WEATHER API) DI SINI
# ====================================================================


if __name__ == '__main__':
    print("🚀 Starter Kit Kantin Kampus REST API siap dijalankan di http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
