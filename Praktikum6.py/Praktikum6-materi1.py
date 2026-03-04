# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Insertion Sort (Ascending)
# ==========================================================

def insertion_sort(data):
    #Loop mulai dari data ke-2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #Simpan nilai yang disisipkan
        j = i - 1 #Index elemen terakhir di bagian kiri

        #Geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j] #Geser elemen ke kanan
            j -= 1
        #Sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))