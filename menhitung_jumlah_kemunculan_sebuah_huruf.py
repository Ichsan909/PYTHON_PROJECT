teks = input("masukkan sebuah kalimat: ")
huruf = input("masukkan huruf yang ingin di hitung: ")

jumlah = teks.lower().count(huruf.lower())
print(f"jumlah huruf '{huruf}' dalam kalimat adalah: {jumlah}")