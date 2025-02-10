def hitung_karakter_unik(teks):
    karakter_unik = set(teks)
    return len(karakter_unik)
teks = input("masukkan string: ")
jumlah_karakter_unik = hitung_karakter_unik(teks)
print(f"jumlah karakter unik dalam string adalah: {jumlah_karakter_unik}")