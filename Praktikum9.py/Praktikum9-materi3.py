# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 3: Membuat Traversal Tree
# ==========================================================

#Class node digunakan untuk dasar dari tree
class node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #Child kiri
        self.right = None   #Chiled kanan

#Fungsi preorder : root ==> left => right
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

#Membuat tree
#Membuat sebuah node root
root = node("A")

#Membuat child level 1
root.left = node("B")
root.right = node("C") 

#Membuat child level 2
root.left.left = node("D")
root.left.right = node("E")

#Menjalankan traversal preorder
print("Preorder Traversal:")
preorder(root)

#Penjelasan
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Fungsi preorder digunakan untuk melakukan traversal pada tree secara preorder, yaitu dengan mengunjungi root, child kiri, lalu child kanan.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "A" dan menyimpannya dalam variabel root.
# Setelah itu, kita menambahkan child kiri dan kanan untuk node root dengan nilai "B" dan "C".
# Kemudian, kita menambahkan child kiri dan kanan untuk node "B" dengan nilai "D" dan "E". 
