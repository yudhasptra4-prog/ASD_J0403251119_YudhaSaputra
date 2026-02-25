# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):              # Membuat fungsi untuk menghasilkan kombinasi biner
    # Base case
    if len(hasil) == n:              # Jika panjang string hasil sudah sama dengan n
        print(hasil)                 # Cetak kombinasi biner yang terbentuk
        return                       # Hentikan proses pada cabang ini

    biner(n, hasil + "0")            # Menambahkan angka 0 lalu memanggil fungsi secara rekursif
    biner(n, hasil + "1")            # Menambahkan angka 1 lalu memanggil fungsi secara rekursif

biner(3)                             # Menjalankan fungsi untuk kombinasi biner sepanjang 3