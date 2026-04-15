# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 2: Membuat Level Node
# ==========================================================

#Class node digunakan untuk dasar dari tree
class node:
    def __init__(self, data):
        self.data = data #Menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Chiled kanan

#Membuat sebuah node root 
root = node("A")

#Membuat child level 1
root.left = node("B")
root.right = node("C")

#Membuat child level 2
root.left.left = node("D")
root.left.right = node("E")

#Membuat child level 2 untuk subtree kanan dari root
root.right.left = node("F")  # Child kiri dari C
root.right.right = node("G") # Child kanan dari C

#Menampilkan isi node
print("Data pada root:", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)
print("Child kiri dari C:", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)

#Penjelasan
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "A" dan menyimpannya dalam variabel root.
# Setelah itu, kita menambahkan child kiri dan kanan untuk node root dengan nilai "B" dan "C".
# Selanjutnya, kita menambahkan child kiri dan kanan untuk node "B" dengan nilai "D" dan "E", serta menambahkan child kiri dan kanan untuk node "C" dengan nilai "F" dan "G".

