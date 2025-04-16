def urut_menurun(daftar):
    return sorted(daftar, reverse=True)

DAFTAR_ANGKA = [5,3,4,5,6,7,7,3,3,7,6,]

hasil = urut_menurun(DAFTAR_ANGKA)
print("daftar angka setelah di urutkan menurun: ")
print(hasil)