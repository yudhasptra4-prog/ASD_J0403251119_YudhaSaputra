#====================================================================
#Nama : Yudha Saputra
#NIM : J0403251119
#Kelas : TPL/B-P2
#Mata Kuliah : Algoritma & Struktur Data
#====================================================================
#Implementasi : Rekursif
#Case : Menghitung jumlah dalam baris
#base case => sampai akhir list
#====================================================================

def jumlah_list(n, index=0):          # Membuat fungsi untuk menjumlahkan seluruh elemen dalam list
    if index == len(n):               # Base case: jika indeks sudah mencapai panjang list
        return 0                      # Kembalikan 0 sebagai nilai awal penjumlahan
    
    # Menjumlahkan elemen dengan hasil penjumlahan elemen berikutnya secara rekursif
    return n[index] + jumlah_list(n, index + 1)  
    
# Memanggil fungsi untuk menghitung total seluruh elemen dalam list dan menampilkan hasilnya
print(jumlah_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  
