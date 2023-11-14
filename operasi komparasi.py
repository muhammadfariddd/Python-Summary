# Operasi Komparasi

# Setiap Hasil Dari Operasi Komparasi Adalah Boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

print (" ")
print ("=========== Lebih Dari >")
hasil = a > 3
print (a ,">" ,3 ,"=",hasil)
hasil = b > 3
print (b ,">" ,3 ,"=",hasil)
hasil = a > 2
print (a ,">" ,2 ,"=",hasil)
hasil = b > 2
print (b ,">" ,2 ,"=",hasil)

print (" ")
print ("=========== Kurang Dari >")
hasil = a < 3
print (a ,"<" ,3 ,"=",hasil)
hasil = b < 3
print (b ,"<" ,3 ,"=",hasil)
hasil = a < 2
print (a ,"<" ,2 ,"=",hasil)
hasil = b < 2
print (b ,"<" ,2 ,"=",hasil)

print (" ")
print ("=========== Lebih Dari Sama Dengan >=")
hasil = a >= 3
print (a ,">=" ,3 ,"=",hasil)
hasil = b >= 3
print (b ,">=" ,3 ,"=",hasil)
hasil = a >= 2
print (a ,">=" ,2 ,"=",hasil)
hasil = b >= 2
print (b ,">=" ,2 ,"=",hasil)

print (" ")
print ("=========== Kurang Dari Sama Dengan <=")
hasil = a <= 3
print (a ,"<=" ,3 ,"=",hasil)
hasil = b <= 3
print (b ,"<=" ,3 ,"=",hasil)
hasil = a <= 2
print (a ,"<=" ,2 ,"=",hasil)
hasil = b <= 2
print (b ,"<=" ,2 ,"=",hasil)

print (" ")
print ("=========== Sama Dengan ==")
hasil = a == 3
print (a ,"==" ,3 ,"=",hasil)
hasil = b == 3
print (b ,"==" ,3 ,"=",hasil)
hasil = a == 2
print (a ,"==" ,2 ,"=",hasil)
hasil = b == 2
print (b ,"==" ,2 ,"=",hasil)

print (" ")
print ("=========== Tidak Sama Dengan !=")
hasil = a != 3
print (a ,"!=" ,3 ,"=",hasil)
hasil = b != 3
print (b ,"!=" ,3 ,"=",hasil)
hasil = a != 2
print (a ,"!=" ,2 ,"=",hasil)
hasil = b != 2
print (b ,"!=" ,2 ,"=",hasil)

print (" ")

# Is Sebagai Komparasi Objek Identity
print ("=========== Object Identity (Is)")
x = 5 #Ini Adalah Assignment Membuat Objek
y = 5
print ("Nilai x = ",x,",id = " ,hex(id(x)))
print ("Nilai y = ",y,",id = " ,hex(id(y)))

hasil = x is y
print ("x is y =",hasil)

print (" ")
x = 5 #Ini Adalah Assignment Membuat Objek
y = 5
print ("Nilai x = ",x,",id = " ,hex(id(x)))
print ("Nilai y = ",y,",id = " ,hex(id(y)))

hasil = x is y
print ("x is y =",hasil)

print (" ")

print ("=========== Object Identity (Is Not)")
x = 5 #Ini Adalah Assignment Membuat Objek
y = 5
print ("Nilai x = ",x,",id = " ,hex(id(x)))
print ("Nilai y = ",y,",id = " ,hex(id(y)))

hasil = x is not y
print ("x is not y =",hasil)

print (" ")
x = 5 #Ini Adalah Assignment Membuat Objek
y = 6
print ("Nilai x = ",x,",id = " ,hex(id(x)))
print ("Nilai y = ",y,",id = " ,hex(id(y)))

hasil = x is not y
print ("x is not y =",hasil)