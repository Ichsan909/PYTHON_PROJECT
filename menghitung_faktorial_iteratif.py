angka = int(input("masukkan bilangan bulat positif: "))
if angka <0:
    print("faktorial tidak didefinisiskan untuk bilangan negatif.")
else:
    faktorial = 1
    for i in range(1, angka + 1):
        faktorial *= i
    print(f"faktorial dari {angka} adalah {faktorial}")