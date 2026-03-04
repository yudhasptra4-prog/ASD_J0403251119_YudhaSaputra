# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Tracing Insertion Sort
# ==========================================================

data = [5, 2, 4, 6, 1, 3]

for i in range(1, len(data)):   # perulangan dimulai dari indeks 1
    key = data[i]               # menyimpan nilai yang akan disisipkan
    j = i - 1                   # indeks sebelumnya
    pergeseran = 0              # menghitung jumlah pergeseran tiap iterasi

    while j >= 0 and data[j] > key:  # kondisi ascending
        data[j + 1] = data[j]        # menggeser elemen ke kanan
        j -= 1
        pergeseran += 1              # menambah hitungan pergeseran

    data[j + 1] = key          # menyisipkan key ke posisi yang benar

    print(f"Setelah iterasi i = {i}, list = {data}, pergeseran = {pergeseran}")

#Soal:
# 1. Tuliskan isi list setelah iterasi i = 1
# Jawaban: Isi list setelah iterasi i = 1 adalah [2, 5, 4, 6, 1, 3]
# 2. Tuliskan isi list setelah iterasi i = 3
#Jawaban: Isi list setelah iterasi i = 3 adalah [2, 4, 5, 6, 1, 3]
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?
# Jawaban: Pergeseran yang terjadi pada iterasi i = 4 yaitu sebanyak 4 kali
