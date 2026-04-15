# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Yudha Saputra
# NIM     : J0403251119
# Kelas   : TPL-B/P2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):

    # dictionary kosong untuk menyimpan data buku
    database_buku = {}

    try:
        # membuka file dengan read
        with open(nama_file, "r") as file:

            # membaca setiap baris dalam file
            for baris in file:
                data = baris.strip().split(",")
                kode = data[0]
                judul = data[1]
                harga = int(data[2])
                # menyimpan ke dictionary
                database_buku[kode] = {
                    "judul": judul,
                    "harga": harga
                }
    # jika file tidak ditemukan
    except FileNotFoundError:
        print(" Waduh, File buku.txt yang kamu cari tidak ditemukan!")

    # mengembalikan dictionary berisi data buku
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
        # constructor untuk node
    def __init__(self, judul):

        # menyimpan judul buku
        self.judul = judul

        # pointer ke node berikutnya
        self.next = None


class LinkedListPromosi:
    def __init__(self):
         self.head = None

    # fungsi untuk menambahkan buku ke daftar promosi
    def tambah_buku_promosi(self, judul):

        # membuat node baru
        node_baru = Node(judul)
        if self.head is None:
            self.head = node_baru

        else:

            # mulai dari node pertama
            current = self.head
            while current.next:
                current = current.next

            # menghubungkan node terakhir dengan node baru
            current.next = node_baru
    
    # fungsi untuk menampilkan seluruh buku promosi
    def tampilkan_promosi(self):

        # jika linked list kosong
        if self.head is None:
            print("Wah, sepertinya belum ada buku promosi.")
            return

        # mulai traversal dari head
        current = self.head

        print("Daftar Buku Promosi: ")

        # melakukan traversal hingga node terakhir
        while current:

            # menampilkan judul buku
            print("-", current.judul)

            # pindah ke node berikutnya
            current = current.next

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []

        # fungsi untuk menambah pelanggan ke antrean (enqueue)
    def tambah_antrean(self, nama_pelanggan):
        self.antrean.append(nama_pelanggan)
        print(nama_pelanggan, "masuk ke antrean.")


    # fungsi untuk melayani pelanggan (dequeue)
    def layani_pelanggan(self):

        # jika antrean kosong
        if len(self.antrean) == 0:
            print("Tidak ada pelanggan dalam antrean.")

        else:

            # menghapus pelanggan paling depan (FIFO)
            pelanggan = self.antrean.pop(0)

            print(pelanggan, "sedang dilayani.")

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    for i in range(1, len(list_harga)):

        # menyimpan nilai yang akan dibandingkan
        key = list_harga[i]
        j = i - 1
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        list_harga[j + 1] = key
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU CEMARA ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == '1':
            print("\nKatalog Buku:")
            for kode, data in data_buku.items():
                print(kode, ",", data["judul"], ",", data["harga"])
            
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            nama = input("Nama Pelanggan: ")
            antrean_toko.tambah_antrean(nama)
            # Tambahkan logika untuk melayani jika diperlukan
            jawab = input("Layani pelanggan sekarang? (y/n): ")

            if jawab == "y":
                antrean_toko.layani_pelanggan()

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih. -Admin Laras:) ")
            break
        else:
            print("Ups, pilihan kamu tidak valid!")

if __name__ == "__main__":
    main()
