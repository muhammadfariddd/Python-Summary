# Date and Time (Exercise )

import datetime as dt

print(" ")

# tanggal = dt.date(2004,11,29)
# print (tanggal)
# print (f"Hari ini adalah hari = {hari_ini:%A}")

# print (" ")

print("Masukkan Tanggal, Bulan, dan Tahun Lahir Anda!")
tanggal = int(input("Tangggal \t= "))
bulan = int(input("Bulan \t\t= "))
tahun = int(input("Tahun \t\t= "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)

print(" ")

print(f"Tanggal lahir anda adalah {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini adalah tanggal {hari_ini}")

print(" ")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_tahun % 365) // 30

print(f"Hari nya adalah {tanggal_lahir:%A}")
print(f"Umur anda adalah {umur_tahun} tahun {umur_bulan_sisa} bulan")
