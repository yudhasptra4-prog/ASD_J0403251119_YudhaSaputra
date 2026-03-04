# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Melengkapi Fungsi Merge
# ==========================================================

def merge(left, right):
    result = []     # list untuk menyimpan hasil penggabungan
    i = 0           # indeks untuk left
    j = 0           # indeks untuk right

    while i < len(left) and j < len(right):
        # kondisi ascending: ambil elemen yang lebih kecil
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # menambahkan sisa elemen yang belum dibandingkan
    result.extend(left[i:])
    result.extend(right[j:])

    return result

#Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# Jawaban: Kondisi agar menjadi ascending adalah dengan menggunakan
# left[i] <= right[j]
# karena kita ingin mengambil nilai yang lebih kecil terlebih dahulu.

# 2. Jelaskan fungsi result.extend().
# Jawaban: Fungsi result.extend() adalah fungsi yang digunakan untuk menambahkan
# seluruh sisa elemen dari list left atau right ke dalam result.
# Digunakan untuk memastikan setelah while selesai, mungkin masih ada
# elemen yang belum diproses.