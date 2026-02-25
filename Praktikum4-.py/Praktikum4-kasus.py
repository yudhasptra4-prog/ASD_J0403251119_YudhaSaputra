#====================================================================
#Nama : Yudha Saputra
#NIM : J0403251119
#Kelas : TPL/B-P2
#Mata Kuliah : Algoritma & Struktur Data
#====================================================================
#Studi kasus : Sistem Antrian Layanan Akademik
#Implementasi Queue =>
#Enqueue : Memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue : Memindahkan pointer front (hapus data dari depan)
#Front-> A -> B -> C -> rear
#====================================================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim   #Menyimpan NIM Mahasiswa
        self.nama = nama #Menyimpan Nama Mahasiswa
        self.next = None #Pointer ke node berikutnya (awal = none)

#2) Mendefinisikan Queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        #Ketika queue kosong maka front = rear = none
        return self.front is None 
    
    #Menambahkan data baru ke bagian belakang (rear) => menambahkan antrian maahassiwa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):
        NodeBaru = Node(nim,nama) #Instantiasi
        #Jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = NodeBaru
            self.rear = NodeBaru
            return
        
        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = NodeBaru
        self.rear = NodeBaru

    #Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong, Tidak ada Mahasiswa yang dilayani")
            return None
        
        #Lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        Node_dilayani = self.front

        #Geser pointer front ke next front
        self.front = self.front.next

        #Jika front menjadi none ( data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        
        return Node_dilayani
    
    def tampilkan(self):
        print("Daftar Antrian Layanan Mahasiswa (Front -> Rear): ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program Utama

def main():

    #Instansiasi queue
    queue = queueAkademik()

    while True:
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            queue.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = queue.dequeue()
            if dilayani:
                print(dilayani.nim)
            print(f"Mahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            queue.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima Kasih")
            break
        else:
            print("Pilihan tidak valid, Silahkan coba lagi 1-4 ")

if __name__ == "__main__":
    main()  