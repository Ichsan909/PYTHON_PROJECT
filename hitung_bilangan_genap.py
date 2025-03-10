def bilangan_genap(daftar_angka):
    jumlah_genap = sum(1 for angka in daftar_angka if angka % 2 == 0)
    return jumlah_genap
daftar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hasil = bilangan_genap(daftar)
print(f"jumlah bilangan genap dalam daftar: {hasil}")