# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):        # Membuat fungsi untuk menghasilkan kombinasi huruf A dan B
    if len(hasil) == n:            # Jika panjang hasil sudah sama dengan n
        print(hasil)               # Cetak kombinasi yang terbentuk
        return                     # Hentikan proses pada cabang ini

    kombinasi(n, hasil + "A")      # Menambahkan huruf A lalu memanggil fungsi secara rekursif
    kombinasi(n, hasil + "B")      # Menambahkan huruf B lalu memanggil fungsi secara rekursif

kombinasi(2)                       # Menjalankan fungsi untuk kombinasi dengan panjang 2