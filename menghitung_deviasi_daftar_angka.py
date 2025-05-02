import math
data = input("Masukkan daftar angka, pisahkan dengan koma: ")
angka = [float(x.strip()) for x in data.split(",")]
rata_rata = sum(angka) / len(angka)
jumlah_selisih_kuadrat = sum((x - rata_rata) ** 2 for x in angka)
deviasi_standar = math.sqrt(jumlah_selisih_kuadrat / (len(angka) - 1))
print(f"Rata-rata: {rata_rata:.2f}")
print(f"Deviasi standar: {deviasi_standar:.2f}")
