def is_palindrome(n):
    return str(n) == str(n)[::-1]  # Cek apakah angka sama jika dibalik


def count_palindromes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_palindrome(num):
            count += 1
    return count


# Input rentang angka dari pengguna
start = int(input("Masukkan angka awal: "))
end = int(input("Masukkan angka akhir: "))

# Hitung jumlah palindrome dalam rentang tersebut
result = count_palindromes(start, end)

print(f"Jumlah angka palindrome antara {start} dan {end} adalah: {result}")
