# Starter Kit Praktikum 07: Networking dan Integrasi API

Selamat datang di repositori **Starter Kit Praktikum 07**!
Gunakan repositori ini sebagai titik awal (*starting point*) untuk sesi live coding bersama Asisten Dosen di laboratorium.

---

## 🚀 Langkah Memulai Praktikum

### 1. Buka Terminal di Folder Starter Kit
```bash
cd starter-kit-p07
```

### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

### 3. Buka File `app.py` di VS Code
Ikuti instruksi Asisten Dosen untuk melengkapi 4 blok kode live coding:
1. **Langkah 1**: Endpoint `GET /api/menu` dan `GET /api/menu/<int:item_id>`
2. **Langkah 2**: Endpoint `POST /api/menu` (Validasi & Status 201)
3. **Langkah 3**: Endpoint `PUT` dan `DELETE`
4. **Langkah 4**: Endpoint Integrasi Eksternal `GET /api/cuaca-kampus`

### 4. Jalankan Server
```bash
python app.py
```
Buka browser di `http://127.0.0.1:5000/` untuk melihat antarmuka dashboard interaktif!
