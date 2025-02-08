def deret_geometri(a, r, n):
    deret = [a*(r ** i) for i in range(n)]
    return deret

a = int(input("masukkan suku pertama: "))
r = int(input("masukkan rasio: "))
n = int(input("masukkan jumlah suku: "))

deret = deret_geometri(a, r, n)
print("deret geometri:", deret)