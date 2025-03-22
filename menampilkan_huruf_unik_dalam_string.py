def huruf_unik(teks):
    unik = []
    for huruf in teks:
        if teks.count(huruf) == 1:
            unik.append(huruf)
    return unik

teks = input("masukkan angka: ")
hasil = huruf_unik(teks)

print("Huruf unik dalam string:", hasil)