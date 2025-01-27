def hitung_digit_ganjil(agka):
    angka_str = str(angka)

    jumlah_ganjil = 0 

    for digit in angka_str:
        if digit.isdigit():
            if int(digit) % 2 != 0:
                jumlah_ganjil += 1
    return jumlah_ganjil

angka = int(input("masukkan sebuah angka: "))
hasil = hitung_digit_ganjil(angka)
print(f"jumlah digit ganjil dalam angka {angka} adalah {hasil}")