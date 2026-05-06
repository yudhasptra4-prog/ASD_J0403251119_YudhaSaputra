#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Latihan 2 :   Implementasi Dijkstra 
#======================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

#1.  Berapa jarak terpendek dari A ke B?
# Jarak terpendek dari A ke B adalah 4.
# Dalam graph, terdapat edge langsung dari A ke B dengan bobot 4, sehingga jarak terpendeknya adalah 4.

#2.  Berapa jarak terpendek dari A ke C?
# Jarak terpendek dari A ke C adalah 2.
# Dalam graph, terdapat edge langsung dari A ke C dengan bobot 2, sehingga jarak terpendeknya adalah 2.

#3.  Berapa jarak terpendek dari A ke D?
# Jarak terpendek dari A ke D adalah 3.
# Terdapat dua jalur dari A ke D: A -> B -> D dengan total bobot 9 (4 + 5) dan A -> C -> D dengan total bobot 3 (2 + 1).
# Algoritma Dijkstra memilih jalur A -> C -> D karena memiliki bobot total yang lebih kecil, yaitu 3.

#4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jarak A ke D lebih kecil melalui C dibandingkan melalui B karena bobot pada edge A ke C (2) dan C ke D (1) lebih kecil dibandingkan dengan bobot pada edge A ke B (4) dan B ke D (5).
# Meskipun jalur A -> B -> D memiliki lebih sedikit edge (2 edge) dibandingkan dengan jalur A -> C -> D (2 edge),
# jalur A -> C -> D memiliki bobot total yang lebih kecil (3) dibandingkan dengan jalur A -> B -> D (9),
# sehingga algoritma Dijkstra memilih jalur A -> C -> D sebagai jalur terpendek.

#5.  Apa fungsi priority_queue dalam algoritma Dijkstra? 
# Fungsi priority_queue dalam algoritma Dijkstra adalah untuk menyimpan node-node yang akan diproses berdasarkan jarak terpendek yang telah ditemukan sejauh ini.
# Priority queue memungkinkan algoritma untuk selalu memproses node dengan jarak terpendek terlebih dahulu, sehingga memastikan bahwa jalur terpendek ditemukan dengan efisien.
# Dalam implementasi ini, priority_queue menggunakan heapq yang merupakan implementasi heap min-heap di Python.

#6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengasumsikan bahwa setelah sebuah node diproses, jarak terpendek ke node tersebut sudah final.
# Jika terdapat edge dengan bobot negatif, maka setelah sebuah node diproses, jarak terpendek ke node tersebut bisa saja berubah jika ditemukan jalur yang lebih pendek melalui edge dengan bobot negatif.
# Hal ini dapat menyebabkan algoritma Dijkstra memberikan hasil yang salah atau tidak optimal, karena tidak dapat menangani perubahan jarak yang terjadi akibat edge dengan bobot negatif. Oleh karena itu, untuk graph dengan bobot negatif, algoritma yang lebih cocok adalah Bellman-Ford.  

