def desimal_ke_biner(angka):
    return bin(angka)[2:]

angka = int(input("masukkan angka desimal: "))
biner = desimal_ke_biner(angka)
print(f"bilangan biner dari {angka} adalah {biner}")