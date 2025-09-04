# Day 2 - Python Basics
# ---------------------
# Latihan sederhana: input nama & jam belajar, lalu cetak pesan motivasi.

# TODO:
# 1. Gunakan input() untuk ambil nama user.
# 2. Gunakan input() untuk ambil jumlah jam belajar (integer).
# 3. Cetak pesan dengan f-string.

# Contoh output:
# Halo Bee, target belajar kamu hari ini: 3 jam.

# Tulis kode di bawah ini 👇

print("=== PROGRAM PERKENALAN DIRI ===")
print("Selamat datang! Mari kita berkenalan.")

nama = input("Masukkan nama kamu: ")
jam_belajar = int(input("Masukkan target jam belajar hari ini: "))

print(f"Halo {nama}, target belajar kamu hari ini adalah {jam_belajar} jam.")