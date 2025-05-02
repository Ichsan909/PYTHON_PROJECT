teks = input("masukka sebuah kalimat: ")
vokal = "aiueoAIUEO"
hasil = ""
for huruf in teks:
    if huruf not in vokal:
        hasil += huruf
print("kalimat setelah huruf vokal di hapus:",hasil)