def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

angka = int(input("masukkan sebuah angka: "))
if is_prima(angka):
    print(f"{angka} adlah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")