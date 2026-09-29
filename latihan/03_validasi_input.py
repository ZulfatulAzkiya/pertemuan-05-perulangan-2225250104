# Latihan 3 - Validasi Input
# Program meminta nilai ujian antara 0 sampai 100.
# Jika tidak valid, input akan diminta kembali.

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")