def hitung_kemunculan_substring(teks, substring):
    jumlah = teks.count(substring)
    return jumlah
teks_utama = input("masukkan teks utama: ")
substring_dicari = input("masukkan substring yang ingin di hitung: ")

jumlah_kemunculan = hitung_kemunculan_substring(teks_utama, substring_dicari)
print(f"substring '{substring_dicari}' muncul sebanyak {jumlah_kemunculan}")