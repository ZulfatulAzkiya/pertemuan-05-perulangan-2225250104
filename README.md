# Pertemuan 05 Perulangan Python

**Nama:** Zulfatul Azkiya
**NIM:** 2225250104
**Kelas:** 3A

## Tujuan

Program ini bertujuan untuk:

* Memahami penggunaan perulangan `for` dan `while` dalam Python.
* Membuat deret aritmetika berdasarkan suku pertama, beda, dan jumlah suku.
* Menghitung jumlah seluruh suku menggunakan perulangan.
* Melakukan validasi agar jumlah suku (`n`) merupakan bilangan bulat positif.

## Cara Menjalankan

Pastikan berada di folder utama project, kemudian jalankan perintah:

```bash
python kuis/kuis2_deret_aritmetika.py
```

Jika menggunakan `python3`, jalankan:

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

Kemudian masukkan:

1. **Suku pertama (`a`)**
2. **Beda (`d`)**
3. **Banyak suku (`n`)**

Contoh:

```text
Deret Aritmetika
Suku pertama a: 2
Beda d: 3
Banyak suku n: 5
Suku ke-1: 2.00
Suku ke-2: 5.00
Suku ke-3: 8.00
Suku ke-4: 11.00
Suku ke-5: 14.00
Jumlah = 40.00
```

## Algoritma Kuis 2

1. Masukkan nilai `a`, `d`, dan `n`.
2. Periksa nilai `n` menggunakan `while`.
3. Jika `n <= 0`, pengguna diminta memasukkan `n` kembali.
4. Inisialisasi `total` dengan nilai 0.
5. Gunakan `for` sebanyak `n` kali.
6. Hitung setiap suku dengan `a + i * d`.
7. Tambahkan setiap suku ke `total`.
8. Tampilkan setiap suku dan jumlah seluruh suku.

## Hasil Pengujian

| No. | Input             | Keluaran yang Diharapkan | Keluaran Aktual | Status   |
| --- | ----------------- | ------------------------ | --------------- | -------- |
| 1   | a=2, d=3, n=5     | Jumlah = 40.00           | Jumlah = 40.00  | Berhasil |
| 2   | a=10, d=-2, n=4   | Jumlah = 28.00           | Jumlah = 28.00  | Berhasil |
| 3   | a=1.5, d=0.5, n=3 | Jumlah = 6.00            | Jumlah = 6.00   | Berhasil |

## Refleksi

Kesalahan yang ditemukan adalah jumlah perulangan dapat tidak sesuai dengan jumlah suku jika batas `range()` salah. Perbaikannya adalah menggunakan `range(n)` sehingga perulangan berjalan tepat sebanyak `n` kali.