def balik_angka(n):
    return int(str(n)[::-2])
angka = int(input(",asukkan angka: "))
hasil = balik_angka(angka)
print("hasil balik angka:", hasil)