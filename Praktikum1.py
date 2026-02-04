#===========================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#===========================================

#membuka file dengan mode read ('r')
#membuka file dalam satu string
with open ("Data Mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

#Membuka file per baris
print("===membaca file per baris===")
jumlah_baris = 0
with open ("Data Mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris +1
        baris = baris
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#===============================================================
#Praktikum 1 : Konsep AD dan File Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#===============================================================

with open ("Data Mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
        nim, nama, nilai = baris.split(",") #memisahkan kolom berdasarkan koma
        print ("NIM :", nim, " Nama:", nama, "Nilai:", nilai)

#===============================================================
#Praktikum 1 : Konsep AD dan File Handling
#Latihan Dasar 3 : Parsing baris menjadi kolom data
#===============================================================

data_list = [] #list untuk menampung data mahasiswa

with open("Data Mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
        nim, nama, nilai = baris.split(",") #memisahkan kolom berdasarkan koma
        #Simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim,nama,int(nilai)])
    
    print("=== Data Mahasiswa dalam LIST ===")
    print(data_list)

    print("=== Jumlah record dalam LIST ===")
    print("Jumlah record:", len(data_list))

    print("=== Menampilkan data record tertentu ===")
    print("Data record pertama:", data_list[0]) #index ke-0 adalah record ke-1

    data_dict = {} #dictionary untuk menampung data mahasiswa
    with open("Data Mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
            nim, nama, nilai = baris.split(",") 

            #Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {
                "nama":nama,
                "nilai":int(nilai)
            }
    print("=== Data Mahasiswa dalam DICTIONARY ===")
    print(data_dict)   