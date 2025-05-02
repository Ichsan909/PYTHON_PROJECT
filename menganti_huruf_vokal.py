teks = input("masukkan kalimat: ")

vokal = "aiueoAIUEO"
hasil = ""
for huruf in teks:
    if huruf in vokal:
        hasil += "*"
    else:
        hasil += huruf
print("hasil setelah di ganti: ", hasil)