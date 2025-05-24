teks = input("masukkan sebuah teks: ")
huruf = input("masukkan huruf yang ingin di cari indexnya: ")

index =0
ditemukan = False

for karakter in teks:
    if karakter == huruf:
        print(f"huruf '{huruf}' di temukan di index ke -{index}")
        ditemukan = True
    index += 1
if not ditemukan:
    print(f"huruf '{huruf}' tidak di temukan dalam teks.")