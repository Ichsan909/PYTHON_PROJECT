def romawi_ke_angka(romawi):
    romawi_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for huruf in reversed(romawi.upper()):
        nilai = romawi_dict.get(huruf, 0)
        if nilai < prev_value:
            total -= nilai
        else:
            total += nilai
        prev_value = nilai

    return total

romawi_input = input("Masukkan angka Romawi: ")
hasil = romawi_ke_angka(romawi_input)

print(f"Angka desimal dari {romawi_input.upper()} adalah: {hasil}")