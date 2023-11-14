# Operasi Yang Dapat Ditambahkan Dengan Penyingkatan
# Operasi Ditambah Dengan Assignment

a = 5 # Adalah Assignment 
print ("Nilai a =",a)

a += 1 # Artinya Adalah a = a + 1
print ("Nilai a += 1, Nilai a Menjadi ",a)

a -= 2 # Artinya Adalah a = a - 2
print ("Nilai a -= 2, Nilai a Menjadi ",a)

a *= 5 # Artinya Adalah a = a * 5
print ("Nilai a *= 5, Nilai a Menjadi ",a)

a /= 2 # Artinya Adalah a = a / 2
print ("Nilai a /= 2, Nilai a Menjadi ",a)


# Modulus dan Floor Division 
b = 10 
print ("\nNilai b =",b)

b %= 3
print ("Nilai b %= 3, Nilai b Menjadi ",b)

b = 10
print ("\nNilai b =",b)

b //= 3
print ("Nilai b //= 3, Nilai b Menjadi ",b)


# Pangkat atau Eksponen 
a = 5
print ("\nNilai a =",a)

a **= 3
print ("Nilai a **= 3, Nilai a Menjadi ",a)


# Operasi Bitwise
# OR 
c = True
print ("\nNilai c =",c)
c |= False
print ("Nilai c |= False, Nilai c Menjadi ",c)
c = False
print ("Nilai c =",c)
c |= False
print ("Nilai c |= False, Nilai c Menjadi ",c)

# AND 
c = True
print ("\nNilai c =",c)
c &= False
print ("Nilai c &= False, Nilai c Menjadi ",c)
c = True
print ("Nilai c =",c)
c &= True
print ("Nilai c &= True, Nilai c Menjadi ",c)

# XOR 
c = True
print ("\nNilai c =",c)
c ^= False
print ("Nilai c ^= False, Nilai c Menjadi ",c)
c = True
print ("Nilai c =",c)
c ^= True
print ("Nilai c ^= True, Nilai c Menjadi ",c)

# Shifting (Geser geser) 
d = 0b0100
print ("\nNilai d = ",format(d,"04b"))
d >>= 2 # Shift Right
print ("Nilai d >>= 2, Nilai d Menjadi",format(d,"04b"))
d <<= 1 # Shift Left
print ("Nilai d <<= 1, Nilai d Menjadi",format(d,"04b"))
