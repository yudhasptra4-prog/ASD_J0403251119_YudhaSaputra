#===============================================================
#Praktikum 2 : Konsep AD dan File Handling (STUDI KASUS)
#Latihan Dasar 4 : Membuat fungsi load data
#===============================================================

#nama_file = "Data Mahasiswa.txt"

def baca_Data_Mahasiswa(nama_file):
    data_dict = {} #dictionary untuk menampung data mahasiswa
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
            nim, nama, nilai = baris.split(",") 
            #Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {
                "nama":nama,
                "nilai":int(nilai)
            }
    return data_dict

#Memanggil fungsi baca_Data_Mahasiswa
buka_data = baca_Data_Mahasiswa("Data Mahasiswa.txt")
print("jumlah data terbaca", len(buka_data))

#===============================================================
#Praktikum 2 : Konsep AD dan File Handling (STUDI KASUS)
#Latihan Dasar 5 : Membuat fungsi menampilkan data
#===============================================================

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print(" Data Kosong ")
        return
    #Membuat header tabel
    print("\n=== Data Mahasiswa ===")
    print(f"{"NIM" : <10} | {"Nama" : <12} | {"Nilai" :>5}")
    print("-" * 33)

    """
    Untuk tampilan yang rapi, atur f-string formating sebagai berikut:
        {"NIM" : <10} artinya:
        tampilkan nim <= rata kiri dengan lebar 10 karakter
        {"Nama" : <12} artinya:
        tampilkan nama <= rata kiri dengan lebar 12 karakter
        {"Nilai" :>5} artinya:
        tampilkan nilai => rata kanan dengan lebar kolom 5 karakter
    """

    for nim in sorted (data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {nilai:>5}")

#Memanggil fungsi tampikan_data
tampilkan_data(buka_data)

#===============================================================
#Praktikum 2 : Konsep AD dan File Handling (STUDI KASUS)
#Latihan 3: Membuat fungsi mencari data
#===============================================================

def cari_data(data_dict):
    #Mencari data mahasiswa berdasarkan nim
    nim_cari = input("Masukkan NIM yang ingin dicari:")

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data Mahasiswa dengan NIM", nim_cari, "tidak ditemukan.")

#cari_data(buka_data)

#===============================================================
#Praktikum 2 : Konsep AD dan File Handling (STUDI KASUS)
#Latihan 4: Membuat fungsi update data
#===============================================================

def update_nilai(data_dict):
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya").strip()
    
    #cari nim yang akan diupdate nilainya
    if nim not in data_dict :
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError: 
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru >100 :
        print("Nilai harus diantara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    #memasukkan nilai update baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhail. nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# update_nilai(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 5 : Membuat Fungsi Menyimpan perubahan data ke file
#-------------------------------------------------------#

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="utf-8") as file :
        for nim in sorted(data_dict.keys()) :
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
        print("Data Berhasil Disimpan")

# simpan_data(nama_file, buka_data)
# print("Data Berhasil Disimpan")

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 6 : Membuat Menu Program
#-------------------------------------------------------#

def main():
    buka_data = baca_Data_Mahasiswa("Data Mahasiswa.txt")

    while True :
        print("\n=== MENU DATA MAHASISWA ")
        print("1. Tampilkan semua data")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilihan Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data("Data Mahasiswa.txt", buka_data)
            print("Data Mahasiswa Tersimpan")
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()