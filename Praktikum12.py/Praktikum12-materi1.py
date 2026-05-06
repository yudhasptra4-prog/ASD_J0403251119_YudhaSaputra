#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Materi 1 : Implementasi Dijkstra dalam Phyton
#======================================================

# Representasi graf menggunakan teknik nested dictionary (kamus bersarang).
# Kunci utama berupa node asal, sedangkan isinya adalah node tujuan beserta bobot nilai (jarak antar node).
import heapq # Modul heapq digunakan untuk mengelola priority queue dalam algoritma Dijkstra.
graph = {
    'A': {'B':4, 'C':2},
    'B': {'D': 5},
    'C': {'D': 1}, 
    'D': {}
}
def dijkstra(graph, start): # Fungsi untuk menentukan rute dengan total bobot terkecil dari simpul asal ('start') menuju seluruh simpul lainnya yang tersedia pada graf.
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)]

    while pq: # Selama masih ada node yang belum diproses dalam priority queue
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance 
 
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 
 
hasil = dijkstra(graph, 'A') 
print(hasil) 