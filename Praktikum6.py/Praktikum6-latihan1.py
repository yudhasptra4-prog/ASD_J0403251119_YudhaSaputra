# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Memahami Kode Program (Insertion Sort)
# ==========================================================

def insertion_sort(data):
   for i in range(1, len(data)):
        key = data[i]
        j = i - 1
     
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        
        return data

#Soal:

# 1. Mengapa perulangan dimulai dari indeks 1?
#Jawaban:
# Perulangan dimulai dari indeks 1 karena elemen pertama (indeks 0) dianggap sudah dalam keadaan terurut.
# Jika perulangan dimulai dari indeks 0, maka tidak ada elemen sebelumnya yang bisa dibandingkan.
# Oleh karena itu, proses dimulai dari indeks 1 agar setiap elemen dapat dibandingkan dengan bagian yang sudah dianggap terurut.

# 2. Apa fungsi variabel key?
# Jawaban:
#Variabel key berfungsi untuk menyimpan nilai yang sedang diproses
# agar bisa dibandingkan dan disisipkan ke posisi yang tepat.

# 3. Mengapa digunakan while, bukan for?
#Jawaban:
#Digunakan while karena jumlah pergeseran tidak tetap
# dan berhenti berdasarkan kondisi tertentu, bukan dari jumlah perulangan.

# 4. Operasi apa yang terjadi di dalam while?
#Jawaban:
# Yang terjadi di dalam while adalah perbandingan dan pergeseran elemen
#  yang lebih besar ke kanan untuk memberi ruang pada key.