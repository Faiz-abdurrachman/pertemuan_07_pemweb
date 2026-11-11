# Starter Kit Praktikum 07: Networking & Integrasi API

Selamat datang di repositori **Starter Kit Praktikum 07 Pemrograman Web**!  
Repositori ini adalah template awal (*starter kit*) untuk belajar membangun **Headless REST API Flask**, pengujian dengan **Postman / Thunder Client**, integrasi pihak ketiga **Open-Meteo Weather**, dan konsumsi asinkron frontend via **JavaScript `fetch()`**.

---

## ⚡ Panduan Cepat Memulai (Bisa Mandiri Tanpa Mentor)

### 1. Kloning Repositori & Masuk Folder
Buka terminal (CMD / PowerShell / Bash) lalu jalankan:
```bash
git clone https://github.com/Faiz-abdurrachman/pertemuan_07_pemweb.git praktikum-p07
cd praktikum-p07
code .
```

### 2. Buat & Aktifkan Virtual Environment
```bash
# Buat venv
python -m venv .venv

# Aktifkan di Windows (PowerShell / CMD)
.venv\Scripts\activate

# Aktifkan di macOS / Linux
source .venv/bin/activate
```
*(Pastikan muncul tanda `(.venv)` di sebelah kiri prompt terminal).*

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Buka `app.py` di VS Code
Di dalam `app.py`, data in-memory kantin dan helper function sudah disediakan. Kamu tinggal melengkapi 4 slot blok live coding sesuai urutan:
1. **Langkah 1 (Baris ~66)**: Endpoint `GET /api/menu` (semua menu) & `GET /api/menu/<int:item_id>` (detail menu).
2. **Langkah 2 (Baris ~74)**: Endpoint `POST /api/menu` (tambah menu dengan validasi & status 201 Created).
3. **Langkah 3 (Baris ~82)**: Endpoint `PUT` (update data) & `DELETE` (hapus menu).
4. **Langkah 4 (Baris ~90)**: Integrasi eksternal `GET /api/cuaca-kampus` menggunakan library `requests` & Open-Meteo.

### 5. Jalankan Server Backend
```bash
python app.py
```
Server akan aktif di `http://127.0.0.1:5000/`. **Jangan tutup terminal ini** selama pengujian!

---

## 🧪 Alat Pengujian API (Pilih Salah Satu)
1. **Postman Desktop**: Standar industri pengujian API ([unduh postman](https://www.postman.com/downloads/)).
2. **Thunder Client (Rekomendasi Ringan)**: Ekstensi VS Code 1-klik tanpa perlu install aplikasi terpisah dan tanpa login akun. Cukup cari "Thunder Client" di tab Extensions VS Code lalu klik Install!

---

## 🖥️ Antarmuka Dashboard Frontend
Buka tab baru di peramban web:  
👉 **`http://127.0.0.1:5000/dashboard`**

Halaman dashboard ini sudah dilengkapi frontend asinkron `fetch()` yang otomatis menampilkan kartu rekomendasi cuaca kampus dan tabel menu kantin secara real-time tanpa refresh halaman (*zero full-page reload*).
