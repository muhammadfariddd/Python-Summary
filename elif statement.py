# Kalkulator Sederhana

print("\t" + "=" * 50)
print("\t" + " Operator Elif ".center(50, "="))
print("\t" + "=" * 50 + "\n")

angka_1 = int(input("Masukkan Angka Pertama :"))
operator = input("Masukkan Operatornya (+,-,x,/) :")
angka_2 = int(input("Masukkan Angka kedua :"))

print (" ")

# Percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasil Dari Penjumlahan {angka_1} {operator} {angka_2} Adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasil Dari Pengurangan {angka_1} {operator} {angka_2} Adalah : {hasil}")
elif operator == "x" or operator == "X" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasil Dari Perkalian {angka_1} {operator} {angka_2} Adalah : {hasil}")
elif operator == "/" or operator == ":":
    hasil = angka_1 / angka_2
    print(f"Hasil Dari Pembagian {angka_1} {operator} {angka_2} Adalah : {hasil}")
else:
    print("Maaf, Data Yang Anda Masukkan Kurang Tepat")
