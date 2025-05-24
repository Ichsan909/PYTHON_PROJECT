teks = "Halo Dunia!"
konsonan = "bcdfghjklmnpqrstvwxyz"
jumlah = 0

for huruf in teks.lower():
    if huruf in konsonan:
        jumlah += 1
print("jumlah konsosnan:",jumlah)
