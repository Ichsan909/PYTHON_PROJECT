def hitung_jumlah(a, b):
    jumlah = 0
    for i in range(a, b + 1):
        jumlah += i
    return jumlah

# Contoh penggunaan
awal = int(input("Masukkan angka awal: "))
akhir = int(input("Masukkan angka akhir: "))

hasil = hitung_jumlah(awal, akhir)
print(f"Jumlah bilangan dari {awal} sampai {akhir} adalah {hasil}")
