def hitung_frekuensi(daftar):
    frekuensi = {}
    for elemen in daftar:
        if elemen in frekuensi:
            frekuensi[elemen] += 1
        else:
            frekuensi[elemen] = 1
    return frekuensi


daftar_angka = [1, 2, 2, 3, 1, 4, 2, 3, 3, 3]
hasil = hitung_frekuensi(daftar_angka)


for elemen, jumlah in hasil.items():
    print(f"Elemen {elemen} muncul sebanyak {jumlah} kali.")
