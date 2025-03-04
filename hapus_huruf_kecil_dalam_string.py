def hapus_huruf_kecil(s):
    return ''.join(char for char in s if not char.islower())

teks = input("masukkan string: ")
hasil = hapus_huruf_kecil(teks)
print(hasil)