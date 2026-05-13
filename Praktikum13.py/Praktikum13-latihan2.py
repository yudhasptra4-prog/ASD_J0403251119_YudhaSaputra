# ======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 13 - Graph III: Spanning Tree
# ======================================================
# Latihan 2: Implementasi Algoritma Kruskal 
# ======================================================

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 
# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() # Mengurutkan edge berdasarkan bobot terkecil
mst = [] # List untuk menyimpan edge yang termasuk dalam Minimum Spanning Tree (MST)
total_weight = 0
connected = set()
for weight, u, v in edges: 
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 

        connected.add(u) # Menambahkan node u ke set connected
        connected.add(v) # Menambahkan node v ke set connected

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 
print("Total bobot =", total_weight)

# Jawaban Analisis: 
#  1. Edge mana yang dipilih pertama kali? 
# Jawaban : 
# Edge yang dipilih pertama kali adalah (1, 'C', 'D') karena memiliki bobot terkecil yaitu 1.
# Hal ini sesuai dengan prinsip algoritma Kruskal yang memilih edge dengan bobot terkecil terlebih dahulu
# untuk membangun Minimum Spanning Tree (MST).

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Jawaban : 
# Edge dengan bobot paling kecil dipilih lebih dahulu karena algoritma Kruskal bertujuan untuk membangun Minimum Spanning Tree (MST) dengan total bobot yang seminimal mungkin.
# Dengan memilih edge dengan bobot terkecil terlebih dahulu, algoritma memastikan bahwa setiap langkah yang
# diambil akan memberikan kontribusi paling kecil terhadap total bobot MST,
# sehingga hasil akhir dari MST akan memiliki bobot total yang minimal.

# 3. Berapa total bobot MST yang dihasilkan? 
# Jawaban :
# Total bobot MST yang dihasilkan adalah 6.
# Total bobot ini diperoleh dari penjumlahan bobot edge yang termasuk dalam MST,
# yaitu (1, 'C', 'D') dengan bobot 1, (2, 'A', 'C') dengan bobot 2, dan (3, 'B', 'D') dengan bobot 3 (1 + 2 + 3 = 6).

# 4.  Mengapa edge tertentu tidak dipilih? 
# Jawaban :
# Edge tertentu tidak dipilih karena jika edge tersebut dipilih, maka akan membentuk siklus dalam MST.
# Dalam algoritma Kruskal, edge yang membentuk siklus tidak diperbolehkan karena tujuan dari MST adalah untuk menghubungkan semua vertex dengan jumlah edge yang seminimal mungkin tanpa membentuk siklus.
# Misalnya, edge (4, 'A', 'B') tidak dipilih karena jika dipilih, maka akan membentuk siklus antara vertex A, B, dan D yang sudah terhubung melalui edge (3, 'B', 'D') dan (2, 'A', 'C').  
# Edge (5, 'A', 'D') juga tidak dipilih karena jika dipilih, maka akan membentuk siklus antara vertex A, D, dan C yang sudah terhubung melalui edge (1, 'C', 'D') dan (2, 'A', 'C').   

