import csv 
import json
import time
import os
from os import system

print("Selamat Datang Di Video Converter")
time.sleep(3)
print("Dengan Ini Kamu Bisa Mengkonversi File(video) Dengan Extensi Apapun Ke Extensi Yang Kamu Inginkan")
time.sleep(3)
print("Jika File Error Saat Kamu Buka Berati File Yang Kamu Ubah Memang Tidak Cocok")
key = input("Tekan Key Apapun Untuk Melanjutkan = ")

if key == 'a' :
	os.system('cls')
	nama = input("Masukan Nama File = ")
	tension = input("Masukan Extensi File  = ")
	akhir = input("Masukan Nama File Baru = ")
	newtension = input("Masukan Extensi File Baru = ")


	with open(nama+"." + tension, "rb") as read:
		with open(akhir + "." + newtension, "wb") as copy:

			copy.write(read.read())
	print("File Berhasil Di Konversi")
else:
	os.system('cls')
	nama = input("Masukan Nama File = ")
	tension = input("Masukan Extensi File  = ")
	akhir = input("Masukan Nama File Baru = ")
	newtension = input("Masukan Extensi File Baru = ")


	with open(nama+"." + tension, "rb") as read:
		with open(akhir + "." + newtension, "wb") as copy:

			copy.write(read.read())
	print("File Berhasil Di Konversi")