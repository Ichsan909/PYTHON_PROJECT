def cari_faktor(angka):
    faktor = [i for i in range(1, angka + 1) if angka % i == 0]
    return faktor
angka = int(input("masukkan agka: "))
print(f"faktor dari {angka} adalah: {cari_faktor(angka)}")