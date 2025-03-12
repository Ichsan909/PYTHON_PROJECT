def bagi_string(teks, panjang_bagian):
    if panjang_bagian <= 0:
        return "panjang bagian harus lebih dari 0"
    
    hasil = [teks[i:i+panjang_bagian]for i in range(0, len(teks), panjang_bagian)]
    return hasil

teks_input = input("masukkan teks: ")
panjang = 4
hasil_pemecahan = bagi_string(teks_input, panjang)

print(hasil_pemecahan)