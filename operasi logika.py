# Operasi Logika atau Boolean

# Not, Or, And, Xor

print (" ")

# NOT (Kebalikan Dari Data Awal)
print ("======= NOT =======")
a = True
b = not a
print ("data a : ",a)
print ("----------------NOT")
print ("data b : ",b)

print (" ")

# OR (Jika Salah Satu True Maka True) 
print ("======= OR =======")
a = True
b = True
c = a or b
print (a," OR",b," =",c)
a = False
b = False
c = a or b
print (a,"OR",b,"=",c)
a = True
b = False
c = a or b
print (a," OR",b,"=",c)
a = False
b = True
c = a or b
print (a,"OR",b," =",c)

print (" ")

# AND (Jika Salah Satu False Maka False) 
print ("======= AND =======")
a = True
b = True
c = a and b
print (a," AND",b," =",c)
a = False
b = False
c = a and b
print (a,"AND",b,"=",c)
a = True
b = False
c = a and b
print (a," AND",b,"=",c)
a = False
b = True
c = a and b
print (a,"AND",b," =",c)

print (" ")

# XOR (Jika Salah Satu Data Beda Maka True) 
print ("======= XOR =======")
a = True
b = True
c = a ^ b
print (a," XOR",b," =",c)
a = True
b = False
c = a ^ b
print (a," XOR",b,"=",c)
a = False
b = True
c = a ^ b
print (a,"XOR",b," =",c)
a = False
b = False
c = a ^ b
print (a,"XOR",b,"=",c)
