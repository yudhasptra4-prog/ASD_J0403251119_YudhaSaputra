#======================================================
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: B-P2
# Praktikum 12 - Graph II: Shortest Path 
#======================================================
# Latihan 5 :   Studi Kasus dengan Program Shortest Path 
#======================================================


import heapq

# 1. Representasi graf menggunakan teknik nested dictionary (kamus bersarang).
#    Kunci utama berupa kota asal, sedangkan isinya adalah kota tujuan 
#    beserta bobot nilai (jarak antarkota).
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta' : {'Bandung': 7},
    'Bandung' : {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Fungsi untuk menentukan rute dengan total bobot terkecil dari simpul 
    asal ('start') menuju seluruh simpul lainnya yang tersedia pada graf.
    """
    # Menetapkan nilai awal tak terhingga untuk seluruh titik tujuan
    distances = {node: float('inf') for node in graph}

    # Menentukan jarak dari titik awal menuju dirinya sendiri sebesar 0
    distances[start] = 0

    # Inisialisasi struktur antrean prioritas (antrean dengan prioritas bobot terkecil)
    # Menyimpan representasi data berpasangan: (bobot_kumulatif, nama_simpul)
    priority_queue = [(0, start)]

    while priority_queue:
        # Mengeluarkan simpul yang memiliki nilai bobot terkecil dari antrean
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati proses jika ditemukan jalur lain yang nilai bobotnya lebih efisien
        if current_distance > distances[current_node]:
            continue

        # Memulai iterasi untuk memeriksa setiap titik tetangga yang terhubung langsung
        for neighbor, weight in graph[current_node].items():
            # Kalkulasi akumulasi bobot baru dari simpul aktif ke simpul tetangga
            distance = current_distance + weight

            # Tahap Relaksasi: Update data jika rute baru ini menghasilkan bobot lebih rendah
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 3. Penentuan titik awal keberangkatan
node_awal = 'Bogor'

# 4. Memproses pencarian jalur dan menyajikan hasil akhir di layar
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"  {node_awal} -> {kota} = {jarak}")


# Jawaban Analisis:

#1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah 'Bogor'.
# Hal ini ditentukan pada bagian kode yang menyatakan node_awal = 'Bogor',
# yang kemudian digunakan sebagai argumen saat memanggil fungsi dijkstra untuk mencari jarak terpendek dari Bogor ke kota-kota lainnya.

#2. Node mana yang memiliki jarak paling kecil dari node awal? 
# Node yang memiliki jarak paling kecil dari node awal 'Bogor' adalah 'Depok' dengan jarak 2.
# Hal ini karena pada graph, terdapat edge langsung dari Bogor ke Depok dengan bobot 2, yang merupakan nilai terkecil dibandingkan dengan edge lainnya dari Bogor.

#3. Node mana yang memiliki jarak paling besar dari node awal? 
# Node yang memiliki jarak paling besar dari node awal 'Bogor' adalah 'Bandung' dengan jarak 7.
# Hal ini karena pada graph, terdapat edge langsung dari Bogor ke Bandung dengan bobot 7, yang merupakan nilai terbesar dibandingkan dengan edge lainnya dari Bogor.
# Meskipun terdapat jalur lain seperti Bogor -> Depok -> Bandung dengan total bobot 8 (2 + 6), jalur tersebut memiliki bobot total yang lebih besar dibandingkan dengan jalur langsung dari Bogor ke Bandung, sehingga jarak terpendek ke Bandung tetap 7.

#4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja dengan cara memulai dari node awal (Bogor) dan secara iteratif mencari node tetangga yang memiliki bobot terkecil untuk mencapai node tujuan.
# Pada setiap langkah, algoritma memeriksa semua tetangga dari node saat ini dan
# menghitung jarak kumulatif ke setiap tetangga. Jika ditemukan jarak yang lebih kecil daripada jarak yang sudah tercatat, maka jarak tersebut diperbarui dan tetangga tersebut dimasukkan ke dalam antrean prioritas untuk diproses selanjutnya.
# Proses ini terus berlanjut hingga semua node telah diproses, sehingga menghasilkan jarak terpendek dari node awal ke semua node lainnya dalam graph. Dalam kasus ini, algoritma Dijkstra berhasil menentukan jarak terpendek dari Bogor ke Jakarta, Depok, dan Bandung dengan benar berdasarkan bobot yang diberikan pada graph.
# Algoritma Dijkstra memastikan bahwa setiap node diproses berdasarkan jarak terpendek yang telah ditemukan sejauh ini, sehingga menghasilkan hasil yang akurat dan efisien untuk graph dengan bobot non-negatif.
# Jika terdapat edge dengan bobot negatif, algoritma Dijkstra tidak akan memberikan hasil yang benar, sehingga dalam kasus ini, Dijkstra adalah pilihan yang tepat karena semua bobot edge bernilai positif.
# pada kasus ini, algoritma Dijkstra berhasil menentukan jarak terpendek dari Bogor ke Jakarta, Depok, dan Bandung dengan benar
# berdasarkan bobot yang diberikan pada graph.
# Algoritma Dijkstra memastikan bahwa setiap node diproses berdasarkan jarak terpendek yang telah ditemukan sejauh ini, sehingga menghasilkan hasil yang akurat dan efisien untuk graph dengan bobot non-negatif.
# Jika terdapat edge dengan bobot negatif, algoritma Dijkstra tidak akan memberikan hasil yang benar
# sehingga dalam kasus ini, Dijkstra adalah pilihan yang tepat karena semua bobot edge bernilai positif.



