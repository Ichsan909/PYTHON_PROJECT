def daftar_unik(daftar):
    unik = []
    for angka in daftar:
        if angka not in unik:
            unik.append(angka)
    return unik

daftar_angka = [4, 2, 2, 4, 5, 6, 7,]
hasil = daftar_unik(daftar_angka)

print("daftar angka dalam element unik: ")
print(hasil)