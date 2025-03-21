def hitung_median(data):
    data.sort()  # Urutkan data terlebih dahulu
    n = len(data)
    tengah = n // 2  # Cari indeks tengah

    if n % 2 == 0:
        # Jika jumlah data genap, median adalah rata-rata dua nilai tengah
        median = (data[tengah - 1] + data[tengah]) / 2
    else:
        # Jika jumlah data ganjil, median adalah nilai tengah
        median = data[tengah]
    
    return median

# Contoh penggunaan
angka = [7, 3, 5, 9, 1]
median = hitung_median(angka)
print("Median:", median)
