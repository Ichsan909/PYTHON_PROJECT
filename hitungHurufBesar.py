def hitung_huruf_besar(teks):
    jumlah_huruf_besar = 0 
    for karakter in teks:
        if karakter.isupper():
            jumlah_huruf_besar += 1
    return jumlah_huruf_besar

input_string = input("masukkan sbuah string: ")
hasil = hitung_huruf_besar(input_string)
print(f"jumlah huruf besar dalam string '{input_string}' adalah {hasil}")