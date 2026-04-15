# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 6: Struktur Organisasi Perusahaan
# ==========================================================

#Class node adalah unit dasar  dari tree
from xml.dom.minidom import Node


class node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #Child kiri
        self.right = None   #Chiled kanan

#Membuat traversal postorder : left ==> right ==> root
#Fungsi preorder : root ==> left => right
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

#Membuat tree struktur organisasi perusahaan
root = node("Direktur")

#Membuat child level 1
root.left = node("Manajer A")
root.right = node("Manajer B")

#Membuat child level 2
root.left.left = node("Staff 1")
root.left.right = node("Staff 2")

root.right.right = node("Staff 3")

#Menjalankan traversal preorder
print("Preorder Traversal:")
preorder(root)

#Penjelasan
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Fungsi preorder digunakan untuk melakukan traversal pada tree secara preorder, yaitu dengan mengunjungi root, child kiri, lalu child kanan.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "Direktur" dan menyimpannya dalam variabel root.
# Setelah itu, kita menambahkan child kiri dan kanan untuk node root dengan nilai "Manajer A" dan "Manajer B".
# Kemudian, kita menambahkan child kiri dan kanan untuk node "Manajer A" dengan nilai "Staff 1" dan "Staff 2", serta menambahkan child kanan untuk node "Manajer B" dengan nilai "Staff 3". 


