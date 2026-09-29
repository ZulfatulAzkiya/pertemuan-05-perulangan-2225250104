# Latihan 1 - Tabel Perkalian
# Program menampilkan perkalian bilangan n dari 1 sampai 10.

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")