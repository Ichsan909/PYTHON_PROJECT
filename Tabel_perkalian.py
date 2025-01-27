def perkalian():
    print("===perkalian====")
    try:
        angka1 = float(input("masukkan angka pertama: "))
        angka2 = float(input("masukkan angka ke dua: "))

        hasil = angka1 * angka2
        print(f"hasil perkalian {angka1} x {angka2} = {hasil}")
    except ValueError:
        print("input harus berupa ngka. silahkan coba lagi!")
perkalian()