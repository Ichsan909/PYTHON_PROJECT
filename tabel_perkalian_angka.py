def tabel_perkalian(angka):
    print(f"tabel perkalian untuk {angka}: ")
    for i in range(1,11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")
try:
   angka = int(input("masukkan angka yang ingin di buat tabel perkalian: "))
   tabel_perkalian(angka)
except ValueError:
    print("harap masukkan angka yan valid")