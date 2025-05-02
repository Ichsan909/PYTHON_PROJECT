alas = float(input("masukkan panjang alas (cm): "))

tinggi_segitiga = float(input("masukkan tinggi segitiga (cm): "))
tinggi_prisma = float(input("masukkan tinggi prisma (cm): "))

luas_alas = 0.5 * alas * tinggi_segitiga
volume = luas_alas * tinggi_prisma

print("\nLuas alas segitiga = {:.2f} cm²".format(luas_alas))
print("Volume prisma segitiga = {:.2f} cm³".format(volume))