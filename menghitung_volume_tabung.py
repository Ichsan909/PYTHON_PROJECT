import math

def hitung_volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari**2 * tinggi

jari_jari = float(input("masukkan jari_jari tabung: "))
tinggi = float(input("masukkan tinggi tabung: "))

volume = hitung_volume_tabung(jari_jari, tinggi)

print(f"volume tabung adalah:  {volume:.2f}")