def bilangan_genap(n):
    return [i for i in range(2, n+1, 2)]
n = int(input("masukkan bilangan n: "))
print("Bilangan genap hingga", n, "adalah:", bilangan_genap(n))