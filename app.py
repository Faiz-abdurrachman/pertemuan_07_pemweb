from flask import Flask, render_template, request, jsonify
import requests

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
@app.route('/api/menu', methods=['GET'])
def get_all_menu():
    """Mengembalikan semua menu kantin dalam format JSON"""
    return jsonify({
        "status": "success",
        "total": len(menu_kantin),
        "data": menu_kantin
    }), 200


@app.route('/api/menu/<int:item_id>', methods=['GET'])
def get_menu_by_id(item_id):
    """Mengembalikan detail menu berdasarkan ID"""
    item = cari_menu_by_id(item_id)
    if not item:
        return jsonify({
            "status": "error",
            "pesan": f"Menu dengan ID {item_id} tidak ditemukan!"
        }), 404

    return jsonify({
        "status": "success",
        "data": item
    }), 200
# ====================================================================


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 2:
# Buat Endpoint POST /api/menu (Tambah Menu Baru dengan Validasi)
# ====================================================================
@app.route('/api/menu', methods=['POST'])
def tambah_menu():
    """Menambahkan menu baru ke database sementara"""
    data = request.get_json()

    # Validasi keberadaan payload JSON
    if not data:
        return jsonify({
            "status": "error",
            "pesan": "Payload request harus berupa format JSON!"
        }), 400

    nama = data.get('nama', '').strip() if isinstance(data.get('nama'), str) else ''
    harga = data.get('harga')
    kategori = data.get('kategori', 'Makanan')
    stok = data.get('stok', 0)

    # Validasi field nama dan harga
    if not nama:
        return jsonify({"status": "error", "pesan": "Nama menu wajib diisi!"}), 400

    if harga is None or not isinstance(harga, (int, float)) or harga <= 0:
        return jsonify({"status": "error", "pesan": "Harga harus berupa angka dan lebih besar dari 0!"}), 400

    # Auto-generate ID baru (ID tertinggi saat ini + 1)
    id_baru = max([item["id"] for item in menu_kantin], default=0) + 1

    menu_baru = {
        "id": id_baru,
        "nama": nama,
        "harga": int(harga),
        "kategori": kategori,
        "stok": int(stok)
    }

    menu_kantin.append(menu_baru)

    return jsonify({
        "status": "success",
        "pesan": f"Menu '{nama}' berhasil ditambahkan ke kantin!",
        "data": menu_baru
    }), 201
# ====================================================================


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 3:
# Buat Endpoint PUT /api/menu/<int:item_id> & DELETE /api/menu/<int:item_id>
# ====================================================================
@app.route('/api/menu/<int:item_id>', methods=['PUT'])
def update_menu(item_id):
    """Memperbarui informasi menu (harga / stok / nama)"""
    item = cari_menu_by_id(item_id)
    if not item:
        return jsonify({"status": "error", "pesan": f"Menu dengan ID {item_id} tidak ditemukan!"}), 404

    data = request.get_json() or {}

    if 'nama' in data and data['nama'].strip():
        item['nama'] = data['nama'].strip()

    if 'harga' in data and isinstance(data['harga'], (int, float)) and data['harga'] > 0:
        item['harga'] = int(data['harga'])

    if 'stok' in data and isinstance(data['stok'], int) and data['stok'] >= 0:
        item['stok'] = int(data['stok'])

    return jsonify({
        "status": "success",
        "pesan": f"Menu '{item['nama']}' berhasil diperbarui!",
        "data": item
    }), 200


@app.route('/api/menu/<int:item_id>', methods=['DELETE'])
def hapus_menu(item_id):
    """Menghapus menu berdasarkan ID"""
    item = cari_menu_by_id(item_id)
    if not item:
        return jsonify({"status": "error", "pesan": f"Menu dengan ID {item_id} tidak ditemukan!"}), 404

    menu_kantin.remove(item)
    return jsonify({
        "status": "success",
        "pesan": f"Menu '{item['nama']}' berhasil dihapus dari sistem kantin!"
    }), 200
# ====================================================================


# ====================================================================
# LIVE CODING PRAKTIKUM 07 - LANGKAH 4:
# Integrasi API Eksternal: GET /api/cuaca-kampus via Open-Meteo
# ====================================================================
@app.route('/api/cuaca-kampus', methods=['GET'])
def get_cuaca_kampus():
    """Mengambil cuaca real-time dari satelit Open-Meteo dan memberikan rekomendasi hidangan kantin"""
    url = "https://api.open-meteo.com/v1/forecast?latitude=-7.8014&longitude=110.3647&current_weather=true&timezone=Asia%2FBangkok"

    try:
        # Panggil API luar dengan batas waktu 5 detik
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        weather_data = response.json()
        current_weather = weather_data.get("current_weather", {})
        suhu = current_weather.get("temperature", 28.0)

        # Logika rekomendasi berdasarkan suhu aktual
        if suhu >= 30.0:
            rekomendasi = "Cuaca terik banget! Rekomendasi: Es Teh Manis Jumbo segar!"
        elif suhu <= 25.0:
            rekomendasi = "Cuaca sejuk / gerimis dingin. Rekomendasi: Mie Ayam Bakso Kuah Panas!"
        else:
            rekomendasi = "Cuaca hangat bersahabat! Semua hidangan kantin siap dinikmati."

        return jsonify({
            "status": "success",
            "sumber": "Open-Meteo Free Global Weather API",
            "lokasi": "Kampus Utama (Yogyakarta)",
            "kondisi": "Cerah Berawan",
            "suhu_celcius": suhu,
            "kecepatan_angin_kmh": current_weather.get("windspeed", 0),
            "rekomendasi_menu": rekomendasi
        }), 200

    except requests.RequestException as e:
        # Perlindungan sistem (Graceful Fallback) jika internet lab offline
        return jsonify({
            "status": "fallback",
            "sumber": "Data Cadangan Server Lokal (Offline Mode)",
            "lokasi": "Kampus Utama (Jakarta)",
            "kondisi": "Data Cadangan",
            "suhu_celcius": 28.5,
            "kecepatan_angin_kmh": 5.0,
            "rekomendasi_menu": "Cuaca nyaman! Es Teh Manis Jumbo selalu jadi pilihan aman mahasiswa.",
            "keterangan": "Gagal terhubung ke Open-Meteo, data fallback diaktifkan otomatis."
        }), 200
# ====================================================================


if __name__ == '__main__':
    print("🚀 Starter Kit Kantin Kampus REST API siap dijalankan di http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
