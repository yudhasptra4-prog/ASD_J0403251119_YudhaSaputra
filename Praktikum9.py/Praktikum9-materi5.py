# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 5: Membuat Traversal Postorder
# ==========================================================

#Class node adalah unit dasar  dari tree
class node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #Child kiri
        self.right = None   #Chiled kanan

#Membuat traversal postorder : left ==> right ==> root
def postorder(root):
    if root is not None:
         postorder(root.left)
         postorder(root.right)
         print(root.data, end=" ")

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
print("Postorder Traversal:")
postorder(root)

#Penjelasan
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Fungsi postorder digunakan untuk melakukan traversal pada tree secara postorder, yaitu dengan mengunjungi child kiri, child kanan, lalu root.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "A" dan menyimpannya dalam variabel root.
# Setelah itu, kita menambahkan child kiri dan kanan untuk node root dengan nilai "B" dan "C".
# Kemudian, kita menambahkan child kiri dan kanan untuk node "B" dengan nilai "D" dan "E".