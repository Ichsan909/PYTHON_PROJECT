def hapus_huruf_ganda(teks):
    hasil = ""
    for huruf in teks:
        if huruf not in hasil:
            hasil += huruf
    return hasil
input_pengguna = input("masukkan sebuag string: ")
output = hapus_huruf_ganda(input_pengguna)
print("string setelah menghapus huruf ganda:", output)