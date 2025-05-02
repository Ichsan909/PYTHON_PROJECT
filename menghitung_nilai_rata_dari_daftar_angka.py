data = input("masukkandaftar angka, pisahkan dengan koma (contoh: 70, 80 ,90: )")
angka_list = [float(angka.strip()) for angka in data.split(",")]
jumlah = sum(angka_list)
rata_rata = jumlah / len(angka_list)

print("\njumlah angka =", jumlah)
print("banyaknya data =", len(angka_list))
print("rata_rata nilai = {:.2f}".format(rata_rata))

