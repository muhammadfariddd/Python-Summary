# # latihan Perulangan (Loop)

# # for kondisi :
# # aksi


# # Menggunakan List
# angka_list = [0, 1, 2, 3, 4]  # Ini Adalah List

# print(" Menggunakan List ".center(30, "="))
# for i in angka_list:
#     print(f"i sekarang -> {i}")

# print(" ")


# # Menggunakan Range
# angka_range = range(5)

# print(" Menggunakan Range ".center(30, "="))
# for i in angka_range:
#     print(f"i sekarang -> {i}")

# print(" ")

# angka_range = range(5, 10)

# print(" Menggunakan Range ".center(30, "="))
# for i in angka_range:
#     print(f"i sekarang -> {i}")

# print(" ")


# # Menggunakan String
# data_str = "Hello Hesti Cantik"

# print(" Menggunakan String ".center(30, "="))
# for str in data_str:
#     print(str)


 # Menghitung bilangan faktorial

print("\t" + "=" * 51)
print("\t" + " Program Loop Dengan Inputan ".center(51, "="))
print("\t" + "=" * 51 + "\n")

nama = input("Masukkan nama anda : ")
bilangan = int(input("Masukkan sebuah bilangan : "))

print (" ")

faktorial = 1

if bilangan < 0:
    print(f"Hallo {nama}")
    print(f"Maaf, Faktorial dari bilangan {bilangan} tidak dapat dihitung dikarenakan bilangan negatif")

elif bilangan == 0:
    print(f"Hallo {nama}")
    print(f"Faktorial dari bilangan {bilangan} adalah 1")

else :
    print(f"Hallo {nama}")
    for i in range(1, bilangan + 1):
        faktorial *= i
    print(f"Faktorial dari bilangan {bilangan} adalah {faktorial}")
