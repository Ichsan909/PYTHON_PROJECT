teks = "H4lo Dunia 2025!"
hasil = ""

for huruf in teks:
    if not huruf.isdigit():
        hasil += huruf
print("hasil tanpa angka:", hasil)