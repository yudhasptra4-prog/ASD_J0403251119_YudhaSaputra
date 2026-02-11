# ======================================================
# Nama  : Yudha Saputra
# Mata Kuliah : Algoritma & Struktur Data
# ======================================================

# ======================================================
# LATIHAN 1
# Menghapus node dengan nilai tertentu (Single Linked List)
# ======================================================

class Node:
    def __init__(self, data):
        self.data = data            # menyimpan nilai data
        self.next = None            # pointer ke node berikutnya


class SingleLinkedList:
    def __init__(self):
        self.head = None            # node pertama linked list

    def insert_at_end(self, data):
        new_node = Node(data)       # membuat node baru

        if not self.head:           # jika list kosong
            self.head = new_node
            return

        temp = self.head            # mulai dari head
        while temp.next:            # cari node terakhir
            temp = temp.next
        temp.next = new_node        # sambungkan node terakhir ke node baru

    def delete_node(self, key):
        temp = self.head            # pointer awal dari head

        if temp and temp.data == key:   # jika node pertama adalah key
            self.head = temp.next       # head berpindah
            temp = None                 # hapus node
            return

        prev = None                     # menyimpan node sebelumnya
        while temp and temp.data != key:
            prev = temp                 # simpan node sebelumnya
            temp = temp.next            # lanjut ke node berikutnya

        if temp is None:                # jika data tidak ditemukan
            return

        prev.next = temp.next           # lewati node yang dihapus
        temp = None                     # hapus node
