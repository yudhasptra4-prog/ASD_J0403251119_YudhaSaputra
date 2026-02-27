# ======================================================
# Nama  : Yudha Saputra
# Mata Kuliah : Algoritma & Struktur Data
# ======================================================

# ======================================================
# LATIHAN 5
# Reverse Single Linked List tanpa membuat list baru
# ======================================================
class Node:
    def __init__(self, data):
        self.data = data            # menyimpan nilai data
        self.next = None            # pointer ke node berikutnya


class SingleLinkedList:
    def __init__(self):
        self.head = None            # node pertama

    def append(self, data):
        new_node = Node(data)       # membuat node baru

        if not self.head:           # jika list kosong
            self.head = new_node
            return

        temp = self.head            # mulai dari head
        while temp.next:            # cari node terakhir
            temp = temp.next
        temp.next = new_node        # sambungkan node terakhir

    def print_list(self):
        temp = self.head            # pointer traversal
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None                 # menyimpan node sebelumnya
        current = self.head         # node yang sedang diproses

        while current:
            next_node = current.next    # simpan node berikutnya
            current.next = prev         # balik arah pointer
            prev = current              # geser prev
            current = next_node         # geser current

        self.head = prev                 # update head


# Contoh penggunaan Latihan 5
sll = SingleLinkedList()
elements = [1, 2, 3, 4, 5]

print("\nMasukkan elemen untuk Linked List:", elements)

for el in elements:
    sll.append(el)

print("Linked List sebelum dibalik:", end=" ")
sll.print_list()

sll.reverse()

print("Linked List setelah dibalik:", end=" ")
sll.print_list()