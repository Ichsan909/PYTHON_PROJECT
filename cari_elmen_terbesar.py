def cari_elmen_terbesar(daftar):
    elmen_terbesar = daftar[0]

    for elmen in daftar:
        if elmen > elmen_terbesar:
            elmen_terbesar = elmen
    
    return elmen_terbesar

daftar_Angka =[3, 4, 6, 8, 9]
terbesar = cari_elmen_terbesar(daftar_Angka)
print(f"elmen terbesar dalam daftar adalah: {terbesar}")