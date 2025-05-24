teks = "saya suka makan nasi dan saya suka inum teh"
kata_list = teks.split()
frekuensi = {}

for kata in kata_list:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1
kata_terbanyak = max(frekuensi, key=frekuensi.get)
jumlah = frekuensi[kata_terbanyak]

print("kata yang palaing banyak muncul:", kata_terbanyak)
print("jumlah kemunculan:", jumlah)