#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
#======================================================

import heapq 

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
    'Perpustakaan': {'Lab': 3}, 
    'Kantin': {'Lab': 4, 'Aula': 7}, 
    'Lab': {'Aula': 1}, 
    'Aula': {} 
} 

def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    priority_queue = [(0, start)] 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        if current_distance > distances[current_node]: 
            continue 
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 
hasil = dijkstra(graph, 'Gerbang') 
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit") 

# Jawaban Analisis:

#1. Lokasi mana yang paling dekat dari Gerbang?
# Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
# Hal ini karena pada graph, terdapat edge langsung dari Gerbang ke Kantin dengan bobot 2,
# yang merupakan nilai terkecil dibandingkan dengan edge lainnya dari Gerbang.

#2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
# Jalur terpendeknya adalah Gerbang -> Kantin -> Lab -> Aula dengan total waktu tempuh 2 + 4 + 1 = 7 menit.
# Meskipun terdapat jalur lain seperti Gerbang -> Perpustakaan -> Lab -> Aula, jalur tersebut memiliki waktu tempuh yang lebih lama yaitu 6 + 3 + 1 = 10 menit, sehingga tidak dipilih sebagai jalur terpendek.

#3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# Jalur langsung tidak selalu menghasilkan jarak paling kecil karena bobot pada setiap edge dapat bervariasi.
# Sebuah jalur dengan lebih banyak edge bisa memiliki bobot total yang lebih kecil dibandingkan dengan jalur yang memiliki lebih sedikit edge tetapi bobotnya lebih besar.
# Dalam kasus ini, meskipun terdapat jalur langsung dari Gerbang ke Perpustakaan dengan bobot 6, jalur tersebut tidak dipilih sebagai jalur terpendek ke Aula karena total waktu tempuhnya lebih lama dibandingkan dengan jalur yang melalui Kantin dan Lab. 
# Oleh karena itu, dalam menentukan jalur terpendek, kita harus mempertimbangkan bobot pada setiap edge, bukan hanya jumlah edge yang dilalui.

#4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? 
# Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graph yang digunakan bersifat berbobot (weighted graph) dan semua bobot edge bernilai positif. Algoritma Dijkstra dirancang untuk menemukan jalur terpendek dalam graph berbobot dengan bobot positif, sehingga sangat sesuai untuk menghitung waktu tempuh terpendek antar lokasi di kampus.    
# Selain itu, Dijkstra juga efisien dalam hal waktu komputasi untuk graph dengan jumlah node yang tidak terlalu besar, seperti pada kasus ini, sehingga dapat memberikan hasil dengan cepat dan akurat.
# Jika terdapat edge dengan bobot negatif, maka algoritma Dijkstra tidak akan memberikan hasil yang benar, sehingga dalam kasus ini, Dijkstra adalah pilihan yang tepat karena semua bobot edge bernilai positif.
