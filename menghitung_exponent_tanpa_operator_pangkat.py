bilangan = int(input("masukkan bilangan basis: "))
pangkat = int(input("masukkan pangkat (eksponen): "))
hasil = 1
for i in range(abs(pangkat)):
    hasil *= bilangan
if pangkat < 0:
    hasil = 1 / hasil
print(f"{bilangan} pangakat {pangkat} dalah {hasil}")