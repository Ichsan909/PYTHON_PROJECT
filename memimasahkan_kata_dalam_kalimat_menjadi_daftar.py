def pisah_kata(kalimat):
    return kalimat.split()
kalimat = input("masukkan kalimat: ")
hasil = pisah_kata(kalimat)

print("daftar kata:", hasil)