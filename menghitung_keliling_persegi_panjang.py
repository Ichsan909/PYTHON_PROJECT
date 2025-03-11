def hitunh_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

panjang = float(input("masukkan panjang: "))
lebar = float(input("masukkan lebar: "))

keliling = hitunh_keliling(panjang, lebar)

print(f"keliling persegi panjang adalah: {keliling}")