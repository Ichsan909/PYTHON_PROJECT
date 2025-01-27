def menghitung_kata():
    print("==program hitung kata==")

    teks = input("masukkan kalimat atau teks: ")

    jumlah_kata = len(teks.split())

    print(f"jumlah kata dalam teks tersebut adalah: {jumlah_kata}")

menghitung_kata()