#====================================================================
#Nama : Yudha Saputra
#NIM : J0403251119
#Kelas : TPL/B-P2
#Mata Kuliah : Algoritma & Struktur Data
#====================================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
#====================================================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, no, nama, servis):
        self.no = no # Menyimpan nomor antrian pelanggan
        self.nama = nama # Menyimpan nama pelanggan
        self.servis = servis # Menyimpan jenis servis yang dipilih pelanggan
        self.next = None # Pointer ke node berikutnya (awal bernilai None)

#2) Mendefinisikan Queue, terdiri dari front dan rear
class QueueBengkel:
    def __init__(self):
        self.front = None # Pointer ke node paling depan (pelanggan pertama)
        self.rear = None # Pointer ke node paling belakang (pelanggan terakhir)

    def enqueue(self, no, nama, servis):
        # Membuat node baru berdasarkan data pelanggan
        node_baru = Node(no, nama, servis)
        if self.front is None: # Mengecek apakah antrian masih kosong
            # Jika kosong, node baru menjadi front dan rear
            self.front = node_baru
            self.rear = node_baru
        else:
            # Jika tidak kosong, sambungkan node terakhir
            # dengan node baru
            self.rear.next = node_baru
            
            # Pindahkan pointer rear ke node baru
            self.rear = node_baru

        # Pesan konfirmasi bahwa data berhasil ditambahkan
        print("Pelanggan berhasil ditambahkan ke antrian.")

    def dequeue(self):
        # Mengecek apakah antrian kosong
        if self.front is None:
            print("Antrian kosong, tidak ada pelanggan yang dilayani.")
            return
        dilayani = self.front # Menyimpan node terdepan yang akan dilayani
        self.front = self.front.next # Memindahkan pointer front ke node berikutnya

        # Jika setelah dequeue antrian menjadi kosong
        if self.front is None:
            # rear juga harus di-set ke None
            self.rear = None

        # Menampilkan data pelanggan yang sedang dilayani
        print("Melayani Pelanggan:")
        print("No Antrian :", dilayani.no)
        print("Nama       :", dilayani.nama)
        print("Servis     :", dilayani.servis)

    def tampilkan(self):
        # Mengecek apakah antrian kosong
        if self.front is None:
            print("Antrian masih kosong.")
            return

        # Pointer sementara untuk traversal
        current = self.front

        # Menampilkan seluruh isi antrian
        print("\nDaftar Antrian Pelanggan:")
        while current is not None:
            print("-------------------------")
            print("No Antrian :", current.no)
            print("Nama       :", current.nama)
            print("Servis     :", current.servis)
            
            # Pindah ke node berikutnya
            current = current.next

#Program utama
def main():
    # Membuat objek QueueBengkel
    q = QueueBengkel()

    # Perulangan menu utama
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        # Input pilihan menu dari pengguna
        pilih = input("Pilih menu: ")

        # Menu tambah pelanggan
        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)

        # Menu layani pelanggan
        elif pilih == "2":
            q.dequeue()

        # Menu melihat seluruh antrian
        elif pilih == "3":
            q.tampilkan()

        # Menu keluar program
        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid")
if __name__ == "__main__":
    main()