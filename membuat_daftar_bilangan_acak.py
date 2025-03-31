import random

def buat_daftar(jumlah, batas_bawah, batas_atas):
    return [random.randint(batas_bawah, batas_atas) for i in range(jumlah)]

if __name__ == "__main__":
    jumlah = int(input("masukkan jumlah bilangan acak: "))
    batas_bawah = int(input("masukkan batas bawah: "))
    batas_atas = int(input("masukkan batas atas: "))

    daftar_bilangan = buat_daftar(jumlah, batas_bawah, batas_atas)
    print("daftar bilangan acak:", daftar_bilangan)