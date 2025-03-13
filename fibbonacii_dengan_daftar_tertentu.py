def fibbonacci(n):
    if n <= 0:
        return "jumlah elmen harus lebih dari 0"
    
    fibo_list = [0,1]
    for _ in range(2, n):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list[:n]

jumlah = int(input("masukkan angka: "))
hasil = fibbonacci(jumlah)
print(hasil)