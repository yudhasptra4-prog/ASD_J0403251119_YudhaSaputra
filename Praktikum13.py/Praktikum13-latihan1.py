# ======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 13 - Graph III: Spanning Tree
# ======================================================
# Latihan 1: Implementasi Kruskal 
# =====================================================

# Daftar edge graph 
edges = [ 
    ('A', 'B'), 
    ('A', 'C'), 
    ('A', 'D'), 
    ('C', 'D'), 
    ('B', 'D') 
] 
# Contoh spanning tree 
spanning_tree = [ 
    ('A', 'C'), 
    ('C', 'D'), 
    ('D', 'B') 
] 
print("Edge pada graph:") 
for edge in edges: # Menampilkan semua edge pada graph
    print(edge) 
print("\nSpanning Tree:") 

for edge in spanning_tree: # Menampilkan edge yang termasuk dalam spanning tree
    print(edge) 
print("\nJumlah edge graph =", len(edges)) 
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:

# 1. Apa perbedaan graph awal dan spanning tree? 
# Jawaban : Perbedaan graph awal dan spanning tree terletak pada jumlah edge yang dimiliki.
# Graph awal memiliki 5 edge, sedangkan spanning tree hanya memiliki 3 edge.
# Spanning tree merupakan subgraph dari graph awal yang menghubungkan semua vertex tanpa membentuk siklus,
# sehingga jumlah edge pada spanning tree selalu lebih sedikit dibandingkan dengan graph awal.

# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# Jawaban : Spanning tree tidak boleh memiliki cycle karena tujuan dari spanning tree adalah untuk menghubungkan semua vertex dengan jumlah edge yang seminimal mungkin.
# Jika spanning tree memiliki cycle, maka akan ada edge yang tidak diperlukan untuk menghubungkan vertex,
# sehingga tidak memenuhi kriteria sebagai spanning tree.
# oleh karena itu, spanning tree harus bebas dari cycle agar dapat dianggap sebagai solusi yang valid untuk menghubungkan semua vertex dalam graph. 

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jawaban : Jumlah edge spanning tree selalu lebih sedikit karena spanning tree merupakan subgraph yang menghubungkan semua vertex dengan jumlah edge yang seminimal mungkin.
# Spanning tree harus menghubungkan semua vertex tanpa membentuk siklus, sehingga jumlah edge pada spanning tree selalu kurang dari jumlah vertex dikurangi satu (|V| - 1).
# Dalam kasus ini, graph awal memiliki 4 vertex (A, B, C, D) sehingga spanning tree hanya dapat memiliki maksimal 3 edge untuk menghubungkan semua vertex tanpa membentuk siklus.
# Oleh karena itu, jumlah edge pada spanning tree selalu lebih sedikit dibandingkan dengan jumlah edge pada graph awal. 


