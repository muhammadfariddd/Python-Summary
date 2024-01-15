data_angka = [1, 5, 2, 3, 2, 4, 7, 4, 3, 1, 8, 9, 0]
print(data_angka)

# Count data
data_angka_4 = data_angka.count(4)
data_angka_3 = data_angka.count(3)

print(f"Jumlah angka 4 adalah = {data_angka_4}")
print(f"Jumlah angka 3 adalah = {data_angka_3}")

print(" ")

# Ambil posisi data (index)
data = ["Javascript", "Python", "C++", "Flutter"]
print(data)

index_python = data.index("Python")
index_c = data.index("C++")
print(f"Index Python = {index_python}")
print(f"Index C++ = {index_c}")

print(" ")

# Mengurutkan data
print(f"Data angka sebelum di sort = \n{data_angka}")
data_angka.sort()
print(f"Data angka setelah di sort = \n{data_angka}")

print(f"Data sebelum di sort = \n{data}")
data.sort()
print(f"Data setelah di sort = \n{data}")

print(" ")

# Membalikkan data (reverse)
data_angka.reverse()
data.reverse()
print(f"Data angka setelah di reverse = \n{data_angka}")
print(f"Data setelah di reverse = \n{data}")
