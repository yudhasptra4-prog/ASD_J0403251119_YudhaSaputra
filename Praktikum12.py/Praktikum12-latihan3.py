#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Latihan 3 :  Implementasi Bellman-Ford 
#======================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

# 1. Berapa bobot langsung dari A ke B? 
#Bobot langsung dari A ke B adalah 5.
#alasannya karena pada graph yang diberikan, terdapat edge langsung dari A ke B dengan bobot 5.
#lanjutan dari A ke B adalah 5, sehingga jarak terpendeknya adalah 5.

#2. Berapa total bobot jalur A -> C -> B?
# Total bobot jalur A -> C -> B adalah 2.
# Dalam graph, terdapat edge dari A ke C dengan bobot 4, dan edge dari C ke B dengan bobot -2.
# Sehingga total bobot untuk jalur A -> C -> B adalah 4 + (-2) = 2.

#3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B.
# Dalam graph, jalur A -> B memiliki bobot langsung sebesar 5, sedangkan
# jalur A -> C -> B memiliki total bobot sebesar 2.
# Oleh karena itu, jalur A -> C -> B menghasilkan jarak yang lebih kecil menuju B dibandingkan dengan jalur A -> B.

#4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini dirancang untuk menangani situasi di mana terdapat edge dengan bobot negatif.
# Algoritma Bellman-Ford melakukan relaksasi pada semua edge sebanyak jumlah node - 1 kali, sehingga dapat menemukan jarak terpendek bahkan jika terdapat edge dengan bobot negatif.
# Selain itu, Bellman-Ford juga dapat mendeteksi adanya siklus negatif dalam graph, yang merupakan kondisi di mana jarak dapat terus berkurang tanpa batas.
# Jika siklus negatif terdeteksi, algoritma akan memberikan peringatan bahwa tidak ada solusi yang valid untuk masalah jalur terpendek. Oleh karena itu, Bellman-Ford sangat berguna untuk graph yang mungkin mengandung edge dengan bobot negatif, sementara algoritma lain seperti Dijkstra tidak dapat menangani kasus tersebut dengan benar.

#5. Apa yang dimaksud dengan proses relaksasi edge?
# Proses relaksasi edge dalam algoritma Bellman-Ford adalah langkah di mana algoritma memeriksa setiap edge dalam graph dan mencoba untuk memperbarui jarak terpendek ke node tetangga jika ditemukan jalur yang lebih pendek melalui edge tersebut.
# Selama proses relaksasi, algoritma memeriksa apakah jarak ke node saat ini sudah diketahui (tidak tak hingga) dan apakah jarak melalui edge tersebut lebih kecil daripada jarak yang sudah tercatat untuk node tetangga.
# Jika kondisi tersebut terpenuhi, maka jarak ke node tetangga diperbarui dengan jarak yang lebih kecil tersebut.
# Proses relaksasi ini dilakukan sebanyak jumlah node - 1 kali untuk memastikan bahwa semua jarak terpendek telah ditemukan, bahkan jika terdapat edge dengan bobot negatif.    
# Proses relaksasi edge adalah inti dari algoritma Bellman-Ford, karena memungkinkan algoritma untuk menemukan jarak terpendek dengan benar, bahkan dalam situasi di mana terdapat edge dengan bobot negatif.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Perbedaan utama antara Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat menangani graph dengan edge yang memiliki bobot negatif, sedangkan Dijkstra tidak dapat menangani kasus tersebut dengan benar.
# Dijkstra menggunakan struktur data priority queue untuk selalu memproses node dengan jarak terpendek terlebih dahulu, sehingga efisien untuk graph dengan bobot non-negatif.
# Sementara itu, Bellman-Ford melakukan relaksasi pada semua edge sebanyak jumlah node - 1 kali, sehingga dapat menemukan jarak terpendek bahkan jika terdapat edge dengan bobot negatif.
# Selain itu, Bellman-Ford juga dapat mendeteksi adanya siklus negatif dalam graph, yang merupakan kondisi di mana jarak dapat terus berkurang tanpa batas, sedangkan Dijkstra tidak memiliki mekanisme untuk mendeteksi siklus negatif.
# Oleh karena itu, Bellman-Ford lebih fleksibel dalam menangani berbagai jenis graph, sementara Dijkstra lebih efisien untuk graph dengan bobot non-negatif.

