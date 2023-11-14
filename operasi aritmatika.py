#Operasi Aritmatika

a = 12
b = 3

#Operasi Penjumlahan +
hasil = a + b
print (a,"+",b,"=",hasil)

# Operasi Pengurangan -
hasil = a - b
print (a,"-",b,"=",hasil)

# Operasi Perkalian *
hasil = a * b
print (a,"*",b,"=",hasil)

# Operasi Pembagian /
hasil = a / b
print (a,"/",b,"=",hasil)

# Operasi Eksponen(Pangkat) **
hasil = a ** b
print (a,"**",b,"=",hasil)

# Operasi Modulus %
hasil = a % b
print (a,"%",b,"=",hasil)

# Operasi Floor Division //
hasil = a // b
print (a,"//",b,"=",hasil)


# Prioritas Operasi / Operation Presedence

'''
    1.()
    2.Eksponen **
    3.Perkalian dan Teman-Teman * / ** % //
    4.Pertambahan dan Pengurangan + - 

'''

x = 2 
y = 3 
z = 4

hasil = x + y * z
print (x,"+",y,"*",z,"=",hasil)

hasil = (x + y) * z
print ("(",x,"+",y,")*",z,"=",hasil)