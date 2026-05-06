#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Materi 2 : Implementasi Bellman Ford pada Phyton
#======================================================

# Representasi graf menggunakan teknik nested dictionary (kamus bersarang).
# Kunci utama berupa node asal, sedangkan isinya adalah node tujuan beserta bobot nilai (jarak antar node).
def bellman_ford(graph, start): 
 
    distances = {node: float('inf') for node in graph} # Semua jarak awal dibuat tak hingga
    distances[start] = 0 # Jarak dari start ke start adalah 0
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
 
        for node in graph: # Periksa semua edge
 
            for neighbor, weight in graph[node].items(): # Jika jarak ke node saat ini sudah diketahui, dan ditemukan jarak yang lebih kecil ke neighbor, maka lakukan update jarak
 
                if distances[node] + weight < distances[neighbor]: # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
 
                    distances[neighbor] = distances[node] + weight # Update jarak ke neighbor
 
    return distances # Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain menggunakan algoritma Bellman-Ford.