kalimat = input("masukkan sebuah kalimat: ")
kata_list = kalimat.split()
hitung_kata = {}

for kata in kata_list:
    if kata in hitung_kata:
        hitung_kata[kata] += 1
    else:hitung_kata[kata] = 1
    
print("\njumlah kemunculan setiap kata (kapitalisasi diperhatikan): ")
for kata, jumlah in hitung_kata.items():
    print(f"{kata} {jumlah}")