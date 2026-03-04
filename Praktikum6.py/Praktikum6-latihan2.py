# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Melengkapi Potongan Kode
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # kondisi ascending: geser jika data sebelumnya lebih besar dari key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # menyisipkan key ke posisi yang benar
        data[j + 1] = key

    return data

#Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
# Jawaban:
# Kondisi agar menjadi sorting ascending yaitu dengan menambahkan data[j] > key
# karena elemen yang lebih besar akan digeser ke kanan.
# 2. Ubah agar menjadi descending.
# Jawaban:
# Untuk mengubah menjadi descending, kondisi diubah menjadi data[j] < key
# karena elemen yang lebih kecil akan digeser ke kanan.