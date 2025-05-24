daftar_buah = ['apel', 'jeruk', 'mangga', 'pisang', 'semangka']

print("Daftar sebelum dihapus:")
for i, buah in enumerate(daftar_buah):
    print(f"{i}: {buah}")

try:
    indeks_yang_ingin_dihapus = int(input("\nMasukkan indeks elemen yang ingin dihapus: "))

    if 0 <= indeks_yang_ingin_dihapus < len(daftar_buah):
        buah_dihapus = daftar_buah.pop(indeks_yang_ingin_dihapus)
        print(f"\nElemen '{buah_dihapus}' di indeks {indeks_yang_ingin_dihapus} telah dihapus.")
    else:
        print("\nIndeks tidak valid!")

except ValueError:
    print("\nInput harus berupa angka!")

print("\nDaftar setelah dihapus:")
for i, buah in enumerate(daftar_buah):
    print(f"{i}: {buah}")
