import math

def kombinasi(n, r):
    if r > n:
        return "nilai r tidak boleh lebih besar dari n"
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input("masukkan nilai n: "))
r = int(input("masukkan nilai r: "))

hasil = kombinasi(n, r)
print(f"C{n}, {r} = {hasil}")