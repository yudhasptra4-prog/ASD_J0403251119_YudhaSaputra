#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Latihan 1 :  Weighted Graph dan Perhitungan Jalur 
#======================================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] 
jalur_2 = graph['A']['C'] + graph['C']['D'] 
print("Jalur 1: A -> B -> D =", jalur_1) # A -> B -> D 
print("Jalur 2: A -> C -> D =", jalur_2) # A -> C -> D

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")


# Jawaban Analisis:

#1. Berapa total bobot jalur A -> B -> D?
# Akumulasi bobot untuk rute A -> B -> D adalah 9.
# Nilai ini didapatkan dari penjumlahan bobot pada setiap transisi edge yang dilewati,
# yaitu dari verteks A ke B bernilai 4, ditambah dari verteks B ke D bernilai 5 (4 + 5 = 9).

#2. Berapa total bobot jalur A -> C -> D?
# Akumulasi bobot untuk rute A -> C -> D adalah 3.
# Hasil tersebut diperoleh dengan menjumlahkan nilai bobot pada edge A ke C sebesar 2, 
# dengan bobot pada edge C ke D sebesar 1(2 + 1 = 3).

#3. Jalur mana yang dipilih sebagai jalur terpendek?
#Jalur yang dipilih adalah A -> C -> D (bobotnya cuma 3).
# Di dalam kode, program membandingkan apakah 9 < 3.
# Karena pernyataan itu salah, program otomatis memilih jalur kedua yang nilainya lebih kecil.

#4  Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit? 
# Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena bobot pada setiap edge dapat bervariasi.
# Sebuah jalur dengan lebih banyak edge bisa memiliki bobot total yang lebih kecil dibandingkan dengan jalur yang memiliki lebih sedikit edge tetapi bobotnya lebih besar.
# Oleh karena itu, dalam menentukan jalur terpendek, kita harus mempertimbangkan bobot pada setiap edge, bukan hanya jumlah edge yang dilalui.
# Misalnya, dalam kasus ini, meskipun jalur A -> B -> D memiliki lebih sedikit edge (2 edge) dibandingkan dengan jalur A -> C -> D (2 edge),
# jalur A -> C -> D memiliki bobot total yang lebih kecil (3) dibandingkan dengan jalur A -> B -> D (9), sehingga jalur A -> C -> D dipilih sebagai jalur terpendek.
