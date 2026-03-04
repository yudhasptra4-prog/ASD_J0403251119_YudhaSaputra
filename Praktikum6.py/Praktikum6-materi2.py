# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Insertion Sort dengan tracing
# ==========================================================

def insertion_sort(data):

    #Melihat data awal
        print("Data Awal : ", data)
        print("="*50)

    #Loop mulai dari data ke-2 (index array ke 1)
        for i in range(1, len(data)):

            key = data[i] #Simpan nilai yang disisipkan
            j = i - 1 #Index elemen terakhir di bagian kiri

            print("Iterasi ke-", i)
            print("Nilai Key = ", key)
            print("Bagian Kiri (terurut) : ", data[:i])
            print("Bagian Kanan (belum terurut) : ", data[i:])

        #Geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j] #Geser elemen ke kanan
            j -= 1

        #Sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan : ", data)
        print("="*50)
        
        return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))