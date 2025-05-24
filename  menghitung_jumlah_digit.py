angka = input("masukkan angka: ")

try:
    int(angka)
    angka_bersih = angka.lstrip('-')
    jumlah_digit = len(angka_bersih)
    print(f"jumlah digit dalam {angka} adlah {jumlah_digit}")
    
except ValueError:
    print("masukkan angka yang benar")