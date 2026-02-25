#====================================================================
#Nama : Yudha Saputra
#NIM : J0403251119
#Kelas : TPL/B-P2
#Mata Kuliah : Algoritma & Struktur Data
#====================================================================
#Materi Rekursif : Faktorial
#recursive case => 3! = 3 x 2 x 1
#base case => 0 berhenti
#====================================================================

def faktorial(n):                 # Membuat fungsi untuk menghitung faktorial suatu bilangan
    # Base case
    if n == 0:                    # Jika n bernilai 0
        return 1                  # Kembalikan 1 karena 0! = 1

    # Recursive case
    return n * faktorial(n - 1)   # Mengalikan n dengan hasil faktorial dari n-1

print("===Program Faktorial===")  # Menampilkan judul program
print(f"Hasil Faktorial: {faktorial(3)}")  # Memanggil fungsi faktorial dan menampilkan hasilnya