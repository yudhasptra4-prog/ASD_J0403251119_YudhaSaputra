# ======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 13 - Graph III: Spanning Tree
# ======================================================
# Latihan 4: Studi Kasus: Jaringan Kabel Antar Gedung
# ======================================================

import heapq  # Library untuk priority queue pada algoritma Prim

# ==========================================
# REPRESENTASI WEIGHTED GRAPH
# ==========================================
# Graph direpresentasikan dalam bentuk dictionary
# Setiap node memiliki tetangga dan bobot edge

graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# ==========================================
# FUNGSI ALGORITMA PRIM
# ==========================================
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk menyimpan edge
    edges = []

    # Memasukkan semua edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total biaya minimum
    total_cost = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sebagai dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total biaya
            total_cost += weight

            # Menambahkan edge baru dari node tersebut
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan MST dan total biaya
    return mst, total_cost


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================
mst, total = prim(graph, 'GedungA')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total)


# Jawaban Analisis:

# 1. Algoritma apa yang digunakan?
# Jawaban: Algoritma yang digunakan adalah Prim's Algorithm, yang merupakan salah satu algoritma untuk mencari Minimum Spanning Tree (MST) pada graph berbobot. 

# 2. Edge mana saja yang dipilih?
# Jawaban: Edge yang dipilih adalah:
# GedungA - GedungC = 2
# GedungC - GedungD = 1
# GedungD - GedungB = 3

# 3. Berapa total biaya minimum?
# Jawaban: Total biaya minimum yang dihasilkan adalah 6, yang merupakan jumlah dari bobot edge yang termasuk dalam MST (2 + 1 + 3 = 6).

# 4. Mengapa MST cocok digunakan pada kasus ini?
# Jawaban: MST cocok digunakan pada kasus ini
# Karena MST dapat menghubungkan semua gedung
# dengan biaya minimum tanpa membentuk siklus,
# sehingga pemasangan kabel menjadi lebih hemat.

