import random

def buat_angka_Acak(start, end):
    return random.randint(start, end)

if __name__ == "__main__":
    start = int(input("masukkan angka awal: "))
    end = int(input("masukkan angka akhir: "))
    angka_random = buat_angka_Acak(start, end)
    print(f"angka acak yang di hasilkan: {angka_random}")