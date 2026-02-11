# ======================================================
# Nama  : Yudha Saputra
# Mata Kuliah : Algoritma & Struktur Data
# ======================================================

# ======================================================
# LATIHAN 3
# Mencari data pada Doubly Linked List
# ======================================================
class Node:
    def __init__(self, data):
        self.data = data            # menyimpan nilai data
        self.next = None            # pointer ke node berikutnya
        self.prev = None            # pointer ke node sebelumnya


class DoublyLinkedList:
    def __init__(self):
        self.head = None            # node pertama
        self.tail = None            # node terakhir

    def insert_at_end(self, data):
        new_node = Node(data)       # membuat node baru

        if not self.head:           # jika list kosong
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   # sambungkan tail ke node baru
            new_node.prev = self.tail   # sambungkan prev node baru
            self.tail = new_node        # update tail

    def search(self, key):
        temp = self.head            # mulai dari head

        while temp:                 # traversal list
            if temp.data == key:    # jika data ditemukan
                return True
            temp = temp.next        # lanjut ke node berikutnya

        return False                # data tidak ditemukan


# Contoh penggunaan Latihan 3
dll = DoublyLinkedList()
elements = [2, 6, 9, 14, 20]

for el in elements:
    dll.insert_at_end(el)

print("Masukkan elemen ke dalam Doubly Linked List:", elements)

key = 9
print("Masukkan elemen yang ingin dicari:", key)

if dll.search(key):
    print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")
