def cari_substring(teks, substring):
     if substring in teks:
           print(f"'{substring}' ditemukan dalam '{teks}' pada indeks {teks.find(substring)}")
     else:
           print(f"'{substring}' tidak ditemukan dalam '{teks}'")


teks = input("Masukkan teks: ")
substring = input("Masukkan substring yang ingin dicari: ")
cari_substring(teks, substring)