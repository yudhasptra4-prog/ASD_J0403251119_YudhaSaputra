# ======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 13 - Graph III: Spanning Tree
# ======================================================
# Latihan 3: Implementasi Algoritma Prim 
# ======================================================

import heapq  # Mengimpor library heapq untuk menggunakan priority queue (antrian prioritas)

# Membuat graph berbentuk dictionary
# Setiap node memiliki tetangga beserta bobot edge-nya
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge dalam bentuk priority queue
    edges = []

    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot MST
    total_weight = 0

    # Perulangan selama masih ada edge di priority queue
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Tandai node sebagai sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total bobot MST
            total_weight += weight

            # Memeriksa semua tetangga dari node baru
            for neighbor, w in graph[v].items():

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Masukkan edge baru ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan MST dan total bobot
    return mst, total_weight


# Memanggil fungsi Prim dengan node awal A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)


# Jawaban Analisis: 
# 1. Node awal apa yang digunakan? 
# Jawaban : Node awal yang digunakan dalam algoritma Prim ini adalah node 'A'.
# Node 'A' dipilih sebagai titik awal untuk membangun Minimum Spanning Tree (MST)
# karena algoritma Prim dapat dimulai dari sembarang node dalam graph, dan dalam kasus ini,
# node 'A' dipilih sebagai titik awal untuk memulai proses pemilihan edge dengan bobot terkecil.

# 2. Edge mana yang dipilih pertama kali? 
# Jawaban : Edge yang dipilih pertama kali adalah (2, 'A', 'C') karena memiliki bobot terkecil yaitu 2.
# Hal ini sesuai dengan prinsip algoritma Prim yang memilih edge dengan bobot terkecil terlebih dahulu
# untuk membangun Minimum Spanning Tree (MST). Edge (2, 'A', 'C') dipilih pertama kali karena menghubungkan node 'A' dengan node 'C' dengan bobot terkecil di antara semua edge yang tersedia dari node 'A'.

# 3. Bagaimana Prim menentukan edge berikutnya? 
# Jawaban : Prim menentukan edge berikutnya dengan memeriksa semua edge yang terhubung ke node yang baru saja ditambahkan ke MST.
# Setelah edge pertama (2, 'A', 'C') dipilih, node 'C' ditambahkan ke MST, dan Prim kemudian memeriksa semua edge yang terhubung ke node 'C', yaitu (1, 'C', 'D').
# Edge (1, 'C', 'D') memiliki bobot terkecil di antara semua edge yang terhubung ke node 'C', sehingga edge tersebut dipilih sebagai edge berikutnya.
# Proses ini berlanjut dengan memeriksa edge yang terhubung ke node 'D' dan seterusnya, selalu memilih edge dengan bobot terkecil yang menghubungkan node yang sudah ada di MST dengan node yang belum ada di MST, hingga semua node terhubung dalam MST.  

# 4. Berapa total bobot MST yang dihasilkan? 
# Jawaban : Total bobot MST yang dihasilkan adalah 6.
# Total bobot ini diperoleh dari penjumlahan bobot edge yang termasuk dalam MST,
# yaitu (2, 'A', 'C') dengan bobot 2, (1, 'C', 'D') dengan bobot 1, dan (3, 'B', 'D') dengan bobot 3 (2 + 1 + 3 = 6).   

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Jawaban : Perbedaan pendekatan Prim dan Kruskal terletak pada cara mereka membangun Minimum Spanning Tree (MST).
# Prim memulai dari satu node dan secara bertahap menambahkan edge dengan bobot terkecil yang menghubungkan node yang sudah ada di MST dengan node yang belum ada di MST, sehingga membangun MST secara terpusat dari satu titik awal.
# Sedangkan Kruskal memulai dengan mengurutkan semua edge berdasarkan bobot terkecil dan kemudian menambahkan edge ke MST jika edge tersebut tidak membentuk siklus, sehingga membangun MST secara global dengan mempertimbangkan semua edge sekaligus.
