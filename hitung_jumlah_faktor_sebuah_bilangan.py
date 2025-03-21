def jumlah_faktor(n):
    jumlah = 0
    for i in range(1, n + 1):
        if n % i == 0:
            jumlah += 1

    return jumlah
bilangan = int(input("masukkan bilangan: "))
print("jumlah faktor:", jumlah_faktor(bilangan))