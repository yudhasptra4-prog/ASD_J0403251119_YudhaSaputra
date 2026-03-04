# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Memahami Kode Program (Merge Sort)
# ==========================================================

def merge_sort(data):
    # Base case: jika panjang data 0 atau 1, data sudah terurut
    if len(data) <= 1:
        return data

    # Membagi data menjadi dua bagian (divide)
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Fungsi memanggil dirinya sendiri (recursion)
    # untuk mengurutkan bagian kiri dan kanan
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Menggabungkan kembali dua bagian yang sudah terurut
    return merge(left_sorted, right_sorted)

# 1. Apa yang dimaksud dengan base case?
# Jawaban: Base case adalah kondisi berhenti pada rekursi.
# Pada kode ini, base case terjadi saat panjang data <= 1,
# karena data dengan 1 elemen sudah pasti terurut.

# 2. Mengapa fungsi memanggil dirinya sendiri?
# Jawaban: Fungsi memanggil dirinya sendiri karena menggunakan konsep rekursi 
# yang bertujuan untuk mengurutkan seluruh data isi list
# sampai mencapai base case.

# 3. Apa tujuan fungsi merge()?
# Jawaban: Tujuan fungsi merge() adalah untuk menggabungkan dua list yang sudah terurut
# menjadi satu list yang tetap dalam keadaan terurut.