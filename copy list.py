a = ["Javascript", "Python", "C++", "Flutter"]
print (a)

b = a # pass by reverense
print (b)

a[1] = "Html"
b.sort()
print (a)
print (b)

print (" ")

# Addres dari kedua list 
print (f"Addres a = {hex(id(a))}")
print (f"Addres b = {hex(id(b))}")

print (" ")

# Membuat list dengan copy 
print ("Mengcopy list menggunakan a.copy")
c = a.copy() # full duplicate / data baru

print (f"Addres a = {hex(id(a))}")
print (f"Addres b = {hex(id(b))}")
print (f"Addres c = {hex(id(c))}")

print (" ")
print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")

print (" ")
print ("Mengubah data ke 2")
a[1] = "Python"
print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")

print (" ")