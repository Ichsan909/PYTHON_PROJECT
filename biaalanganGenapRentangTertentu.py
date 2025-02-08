awal = int(input("masukkan batas awal: "))
akhir = int(input("masukkan batas akhir: "))

bilangan_genap = [i for i in range(awal, akhir +1) if i % 2 == 0]

print("dartar bilangan genap da;am rentang:")
print(bilangan_genap)