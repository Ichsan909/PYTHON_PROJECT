def hitung_pangkat(basis, eksponen):
    hasil = 1
    for _ in range(eksponen):
        hasill *= basis
    return hasil
basis = int(input("masukkan basis (angka yang akan dipangkatkan): "))
eksponen = int(input("masukkan eksponen (pangkat): "))
hasil = hitung_pangkat(basis, eksponen)
print(f"hasil dari {basis} pangkat {eksponen} adalah {hasil}")