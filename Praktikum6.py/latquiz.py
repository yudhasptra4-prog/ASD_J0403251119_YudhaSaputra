# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : [Isi Nama Anda]
# NIM     : [Isi NIM Anda]
# Kelas   : [Isi Kelas Anda]
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. FILE HANDLING & DICTIONARY
# ------------------------------------------------------------------------------
def muat_data_buku(nama_file):
    """
    Fungsi ini digunakan untuk membaca file buku.txt
    lalu menyimpannya ke dalam dictionary.

    Format data pada file:
    kode_buku,judul,harga

    Contoh:
    B01,Algoritma Python,120000
    """

    # dictionary kosong untuk menyimpan data buku
    database_buku = {}

    try:
        # membuka file dengan mode read
        with open(nama_file, "r") as file:

            # membaca setiap baris dalam file
            for baris in file:

                # menghapus spasi / newline lalu memisahkan berdasarkan koma
                data = baris.strip().split(",")

                # mengambil masing-masing data
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
        print("File buku.txt tidak ditemukan!")

    # mengembalikan dictionary berisi data buku
    return database_buku


# ------------------------------------------------------------------------------
# 2. LINKED LIST - MANAJEMEN PROMOSI
# ------------------------------------------------------------------------------

# class Node digunakan untuk membuat elemen pada linked list
class Node:

    # constructor untuk node
    def __init__(self, judul):

        # menyimpan judul buku
        self.judul = judul

        # pointer ke node berikutnya
        self.next = None


# class LinkedListPromosi untuk mengelola daftar promosi
class LinkedListPromosi:

    # constructor linked list
    def __init__(self):

        # head adalah node pertama
        self.head = None


    # fungsi untuk menambahkan buku ke daftar promosi
    def tambah_buku_promosi(self, judul):

        # membuat node baru
        node_baru = Node(judul)

        # jika linked list masih kosong
        if self.head is None:

            # node baru menjadi head
            self.head = node_baru

        else:

            # mulai dari node pertama
            current = self.head

            # mencari node terakhir
            while current.next:
                current = current.next

            # menghubungkan node terakhir dengan node baru
            current.next = node_baru


    # fungsi untuk menampilkan seluruh buku promosi
    def tampilkan_promosi(self):

        # jika linked list kosong
        if self.head is None:
            print("Belum ada buku promosi.")
            return

        # mulai traversal dari head
        current = self.head

        print("Daftar Buku Promosi:")

        # melakukan traversal hingga node terakhir
        while current:

            # menampilkan judul buku
            print("-", current.judul)

            # pindah ke node berikutnya
            current = current.next


# ------------------------------------------------------------------------------
# 3. QUEUE - ANTREAN KASIR
# ------------------------------------------------------------------------------

class AntreanKasir:

    # constructor queue
    def __init__(self):

        # menggunakan list untuk menyimpan antrean
        self.antrean = []


    # fungsi untuk menambah pelanggan ke antrean (enqueue)
    def tambah_antrean(self, nama_pelanggan):

        # menambahkan pelanggan ke belakang antrean
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


# ------------------------------------------------------------------------------
# 4. SORTING - LAPORAN TRANSAKSI
# ------------------------------------------------------------------------------

def urutkan_transaksi(list_harga):
    """
    Fungsi ini mengurutkan data harga transaksi
    menggunakan algoritma Insertion Sort secara ascending.
    """

    # perulangan dimulai dari elemen kedua
    for i in range(1, len(list_harga)):

        # menyimpan nilai yang akan dibandingkan
        key = list_harga[i]

        # indeks sebelumnya
        j = i - 1

        # menggeser elemen yang lebih besar dari key
        while j >= 0 and list_harga[j] > key:

            # menggeser elemen ke kanan
            list_harga[j + 1] = list_harga[j]

            # pindah ke indeks sebelumnya
            j -= 1

        # menempatkan key pada posisi yang benar
        list_harga[j + 1] = key

    # mengembalikan list yang sudah terurut
    return list_harga


# ------------------------------------------------------------------------------
# MAIN PROGRAM - MENU ANTARMUKA
# ------------------------------------------------------------------------------

def main():

    # memuat data buku dari file
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)

    # membuat objek linked list promosi
    list_promosi = LinkedListPromosi()

    # membuat objek antrean kasir
    antrean_toko = AntreanKasir()

    # data transaksi awal
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]


    # loop utama program
    while True:

        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")

        # input pilihan menu
        pilihan = input("Pilih menu (1-5): ")


        # MENU 1: menampilkan katalog buku
        if pilihan == '1':

            print("\nKatalog Buku:")

            # menampilkan isi dictionary
            for kode, data in data_buku.items():
                print(kode, "-", data["judul"], "-", data["harga"])


        # MENU 2: menambah buku promosi
        elif pilihan == '2':

            judul_baru = input("Masukkan judul buku untuk promosi: ")

            # menambahkan ke linked list
            list_promosi.tambah_buku_promosi(judul_baru)

            # menampilkan daftar promosi
            list_promosi.tampilkan_promosi()


        # MENU 3: mengelola antrean kasir
        elif pilihan == '3':

            nama = input("Nama Pelanggan: ")

            # menambah pelanggan ke antrean
            antrean_toko.tambah_antrean(nama)

            jawab = input("Layani pelanggan sekarang? (y/n): ")

            if jawab == "y":
                antrean_toko.layani_pelanggan()


        # MENU 4: menampilkan laporan transaksi terurut
        elif pilihan == '4':

            print("Harga Sebelum Urut:", riwayat_transaksi)

            # memanggil fungsi sorting
            hasil_sort = urutkan_transaksi(riwayat_transaksi)

            print("Harga Sesudah Urut:", hasil_sort)


        # MENU 5: keluar dari program
        elif pilihan == '5':

            print("Program selesai. Terima kasih.")
            break

        # jika input tidak valid
        else:
            print("Pilihan tidak valid!")
# menjalankan program utama
if __name__ == "__main__":
    main()