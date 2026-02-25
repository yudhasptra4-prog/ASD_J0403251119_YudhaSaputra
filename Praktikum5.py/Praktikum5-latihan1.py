# ==========================================================
# Nama : Yudha Saputra
# NIM : J0403251119
# Kelas : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):              # Mendefinisikan fungsi bernama pangkat dengan parameter a (bilangan) dan n (pangkat)
    # Base case
    if n == 0:                  # Kondisi dasar: jika pangkat bernilai 0
        return 1                # Kembalikan nilai 1 karena setiap bilangan berpangkat 0 hasilnya 1
    
    # Recursive case
    return a * pangkat(a, n - 1)  # Memanggil fungsi pangkat secara rekursif dengan nilai n dikurangi 1 kemudian dikali n
                                
print(pangkat(2, 4))            # Memanggil fungsi pangkat dengan a=2 dan n=4,
                        