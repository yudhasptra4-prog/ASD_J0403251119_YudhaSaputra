# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 2: Tracking Rekursi
# ==========================================================

def countdown(n):                 # Mendefinisikan fungsi countdown dengan parameter n
    if n == 0:                    # Base case: jika nilai n adalah 0
        print("Selesai")          # Menampilkan bahwa proses telah selesai
        return                    # Menghentikan pemanggilan fungsi agar tidak berulang

    print("Masuk:", n)            # Menampilkan nilai n saat fungsi mulai dijalankan
    countdown(n - 1)              # Memanggil fungsi secara rekursif dengan nilai n dikurangi 1
    print("Keluar:", n)           # Menampilkan nilai n setelah proses rekursi selesai

countdown(3)                      # Memanggil fungsi countdown dengan nilai awal 3