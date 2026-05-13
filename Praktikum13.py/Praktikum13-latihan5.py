# ================================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 13 - Graph III: Spanning Tree
# ================================================================
# Latihan 5:  Tugas Mandiri: Buat Program MST dengan Kasus Baru
# ================================================================

import heapq  # Library untuk priority queue

# ==========================================
# REPRESENTASI WEIGHTED GRAPH
# ==========================================
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
}

# ==========================================
# IMPLEMENTASI ALGORITMA PRIM
# ==========================================
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot minimum
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            # Menandai node dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST
    return mst, total_weight


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================
mst, total = prim(graph, 'Bogor')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot minimum
print("Total bobot minimum =", total)


# Jawaban Analisis:

# 1. Kasus apa yang dipilih?
# Jawaban:
# Kasus yang dipilih adalah jaringan kabel untuk menghubungkan kota-kota Bogor, Jakarta, Depok, dan Bandung dengan biaya minimum.

# 2. Algoritma apa yang digunakan?
# Jawaban:
# Algoritma yang digunakan adalah Prim's Algorithm, yang merupakan salah satu algoritma untuk mencari Minimum Spanning Tree (MST) pada graph berbobot.

# 3. Edge mana saja yang dipilih dalam MST?
# Jawaban:
# Edge yang dipilih dalam MST adalah:
# Bogor - Depok = 2
# Depok - Jakarta = 3
# Depok - Bandung = 4

# 4. Berapa total bobot MST?
# Jawaban:
# Total bobot MST yang dihasilkan adalah 9, yang merupakan jumlah dari bobot edge yang termasuk dalam MST (2 + 3 + 4 = 9).

# 5. Mengapa edge tertentu tidak dipilih?
# Jawaban:
# Edge tertentu tidak dipilih karena 
# edge tersebut memiliki bobot lebih besar
# atau dapat membentuk siklus sehingga tidak efisien
# untuk MST.

# Contoh:
# Jakarta - Bandung = 6 tidak dipilih
# karena sudah ada jalur lebih murah melalui Depok.
