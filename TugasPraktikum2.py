# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Yudha Saputra
# NIM  : J0403251119
# Kelas: TPL B2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stok_dict = {}  # dictionary untuk menampung data barang
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")

            stok_dict[kode] = {
                "nama": nama,
                "stok": int(stok)
            }
    return stok_dict


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return

    # Header tabel 
    print("\n=== DATA STOK BARANG KANTIN ===")
    print(f"{'Kode':<10} | {'Nama Barang':<12} | {'Stok':>5}")
    print("-" * 33)

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<12} | {stok:>5}")


# -------------------------------
# Fungsi: Cari barang
# -------------------------------
def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        print("\n=== BARANG DITEMUKAN ===")
        print(f"Kode : {kode}")
        print(f"Nama : {stok_dict[kode]['nama']}")
        print(f"Stok : {stok_dict[kode]['stok']}")
    else:
        print("Barang tidak ditemukan.")


# -------------------------------
# Fungsi: Tambah barang
# -------------------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()

    if kode in stok_dict:
        print("Kode barang sudah digunakan.")
        return

    stok_awal = int(input("Masukkan stok awal: "))
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Hapus barang
# -------------------------------
def hapus_barang(stok_dict):
    kode = input("Masukkan kode barang yang ingin dihapus: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    konfirmasi = input("Kamu yakin ingin menghapus barang ini? (y/n): ").strip().lower()
    if konfirmasi == "y":
        del stok_dict[kode]
        print("Barang berhasil dihapus.")
    else:
        print("Penghapusan barang dibatalkan.")


# -------------------------------
# Fungsi: Update stok
# -------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih (1/2): ").strip()
    jumlah = int(input("Masukkan jumlah: "))

    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")
    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")


# -------------------------------
# Fungsi: Simpan ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")
    print("Data berhasil disimpan.")


# -------------------------------
# Program Utama
# -------------------------------
def main():
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Hapus barang")
        print("5. Update stok")
        print("6. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            hapus_barang(stok_barang)
        elif pilihan == "5":
            update_stok(stok_barang)
        elif pilihan == "6":
            simpan_stok(NAMA_FILE, stok_barang)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


# Menjalankan program
if __name__ == "__main__":
    main()
