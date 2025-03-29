def temukan_kata_terpanjang(kalimat):
    kata_kata = kalimat.split()
    kata_terpanjang = max(kata_kata, key=len)
    return kata_terpanjang

teks = "program python sangat menyenangkan"
print("kata terpanjang:", temukan_kata_terpanjang(teks))