import math
def permutasi(n, r):
    if n < r:
        return "nilai n harus lebihbesar atau sama dengan r"
    
    return math.factorial(n) // math.factorial(n - r)

n = int(input("masukkan nilai n : "))
r = int(input("masukkan nilai r: "))
hasil = permutasi(n, r)
print(f"Permutasi P({n}, {r}) = {hasil}")