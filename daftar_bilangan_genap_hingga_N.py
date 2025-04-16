n = int(input("masukkan bilangan n:"))

daftar_genap = []

for i in range(0 , n + 1, 2):
    daftar_genap.append(i)

print("bilangan genap hingga", n, ":", daftar_genap)