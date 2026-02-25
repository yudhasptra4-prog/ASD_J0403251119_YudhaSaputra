# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):        # Membuat fungsi untuk menghasilkan kombinasi PIN
    if len(hasil) == panjang:            # Jika panjang PIN sudah sesuai dengan yang ditentukan
        print("PIN:", hasil)              # Menampilkan PIN yang terbentuk
        return                            # Menghentikan proses pada cabang ini

    for angka in ["0", "1", "2"]:         # Perulangan untuk memilih setiap digit yang tersedia
        buat_pin(panjang, hasil + angka)  # Menambahkan digit lalu memanggil fungsi secara rekursif

buat_pin(3)                               # Menjalankan fungsi untuk membuat PIN 3 digit