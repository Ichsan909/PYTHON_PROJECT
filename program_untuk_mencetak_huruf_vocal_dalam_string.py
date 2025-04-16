def cetak_vokal(teks):
    vokal = "aiueoAIUEO"
    hasil = []
    for huruf in teks:
        if huruf in vokal:
            hasil.append(huruf)
    print("huruf okal dalam string: ")
    print(" ".join(hasil))
input_user = "pemerograman Web Menggunakan Python"
cetak_vokal(input_user)