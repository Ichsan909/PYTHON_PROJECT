def hapus_huruf_kapital(teks):
    hasil = ""
    for karakter in teks:
        if not karakter.isupper():
            hasil += karakter
    return hasil
input_string = input("masukkan sebuah string: ")
hasil = hapus_huruf_kapital(input_string)
print(f"string setelah menghapus huruf kapital: '{hasil}'")