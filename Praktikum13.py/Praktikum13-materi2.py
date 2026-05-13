# ======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 13 - Graph III: Algoritma Prim
# ======================================================
# Materi 2: Implementasi Prim
# =====================================================
import heapq # untuk menggunakan priority queue
 
graph = { # Representasi weighted graph menggunakan dictionary bersarang
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 
 
def prim(graph, start): # Implementasi Prim's Algorithm untuk mencari Minimum Spanning Tree (MST)
 
    visited = set([start]) # Set untuk melacak node yang sudah dikunjungi
 
    edges = [] # Priority queue untuk menyimpan edge yang akan diproses
 
    for neighbor, weight in graph[start].items(): # Menambahkan edge awal ke priority queue
        heapq.heappush(edges, (weight, start, neighbor)) # (bobot, node1, node2)
 
    mst = [] # List untuk menyimpan edge yang termasuk dalam MST
    total_weight = 0 
 
    while edges: # Selama masih ada edge yang bisa diproses
 
        weight, u, v = heapq.heappop(edges) # Mengambil edge dengan bobot terkecil dari priority queue
 
        if v not in visited: # Jika node tujuan belum dikunjungi, tambahkan ke MST
 
            visited.add(v) # Menandai node tujuan sebagai sudah dikunjungi
 
            mst.append((u, v, weight)) 
            total_weight += weight 
 
            for neighbor, w in graph[v].items(): 
 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
 
    return mst, total_weight 
 
 
mst, total = prim(graph, 'A') 
 
print("Minimum Spanning Tree:") 
 
for edge in mst: 
    print(edge) 
 
print("Total bobot =", total)