def deret_aritmatika(a, b, n):
    deret = [a + (i *b) for i in range(n)]
    return deret

a = int(input("masukkan suku pertama(a): "))
b = int(input("masukkan beda (b): "))
n = int(input("masukkan jumlah suku (n): "))

deret = deret_aritmatika(a, b, n)
print("deret aritmatika:", deret)