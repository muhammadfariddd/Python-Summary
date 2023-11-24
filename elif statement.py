# Kalkulator Sederhana 

print ("=" * 15)
print ("Operator Elif")
print ("=" * 15 + "\n")

angka_1 = float(input("Masukkan Angka Pertama :"))
operator = input ("Masukkan Operatornya (+,-,x,/) :")
angka_2 = float(input("Masukkan Angka kedua :"))

# Percabangannya 

if operator == "+" :
    hasil = angka_1 + angka_2
    print (f"hasilnya Adalah : {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print (f"hasilnya Adalah : {hasil}")
elif operator == "x" or operator == "*" :
    hasil = angka_1 * angka_2
    print (f"hasilnya Adalah : {hasil}")
elif operator == "/" or operator == ":" :
    hasil = angka_1 / angka_2
    print (f"hasilnya Adalah : {hasil}")
else :
    print ("Maaf,Data Yang Anda Masukkan Salah")
