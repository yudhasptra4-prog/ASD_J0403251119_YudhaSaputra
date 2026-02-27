# =========================================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# =========================================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# =========================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):   # Membuat fungsi kombinasi biner dengan batas jumlah angka 1
    # Pruning
    if jumlah_1 > batas:                           # Jika jumlah angka 1 melebihi batas
        return                                    # Hentikan proses pada cabang ini

    # Base case
    if len(hasil) == n:                            # Jika panjang hasil sudah sama dengan n
        print(hasil)                               # Cetak kombinasi biner yang memenuhi syarat
        return                                    # Hentikan proses pada cabang ini

    biner_batas(n, batas, hasil + "0", jumlah_1)  # Menambahkan angka 0 tanpa menambah jumlah_1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)  # Menambahkan angka 1 dan menambah jumlah_1
    

biner_batas(4, 2)                                 # Menjalankan fungsi dengan panjang 4 dan batas maksimal 2 angka 1