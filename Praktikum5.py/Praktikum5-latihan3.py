# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):        # Membuat fungsi untuk mencari nilai maksimum dalam list
    # Base case
    if index == len(data) - 1:       # Jika sudah sampai elemen terakhir
        return data[index]           # Kembalikan nilai pada indeks terakhir

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)  # Mencari nilai maksimum dari sisa data
    if data[index] > maks_sisa:      # Membandingkan nilai saat ini dengan nilai maksimum sisa
        return data[index]           # Mengembalikan nilai saat ini jika lebih besar
    else:
        return maks_sisa              # Mengembalikan nilai maksimum dari sisa data

angka = [3, 7, 2, 9, 5]              # List berisi kumpulan angka
print("Nilai maksimum:", cari_maks(angka))  # Menampilkan nilai maksimum dari list