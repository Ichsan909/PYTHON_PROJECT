import random

def tebak_angka():
    angka_rahasia = random.randint(1, 10)
    tebakan = None

    print("selamat dtang di game tebak angka")
    print("saya telah memilih angka antara 1 dan 10. coba tebak!")\
    
    while tebakan != angka_rahasia:
        try:
               tebakan = int(input("masukka tebakan anda: "))
               if tebakan < angka_rahasia:
                    print("tebakan terlalu rendah !")
               elif tebakan > angka_rahasia:
                    print("tebakan terlalu besar! cobalagi")
               else:
                    print("selamat anda menebak dengan benar!!")
        except ValueError:
             print("masukkan angka yang valid!")
if __name__ == "__main__":
     tebak_angka()