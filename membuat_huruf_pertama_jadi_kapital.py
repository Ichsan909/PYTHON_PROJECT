def huruf(teks):
    return ' '.join(kata.capitalize() for kata in teks.split())

kalimat = input("masukkan kalimat: ")
hasil = huruf(kalimat)
print("hasil setelah di ubah:", hasil)