# Latihan 2 - Jumlah Bilangan
# Program menghitung jumlah bilangan dari 1 sampai n.

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")