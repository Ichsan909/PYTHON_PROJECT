def hitung_kuadrat(angka):
    return pow(angka, 2)

if __name__ == "__main__":
    angka = float(input("masukkan angka yang ingin di kuadratkan: "))
    hasil = hitung_kuadrat(angka)
    print(f"kuadrat dari {angka} adalah {hasil}")