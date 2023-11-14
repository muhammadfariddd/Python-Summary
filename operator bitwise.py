# Operator Bitwise


a = 9
b = 5

# Bitwise Or (|)
c = a | b
print ("\n==========OR==========")
print ("Nilai :",a,"Binary :",format(a,"08b"))
print ("Nilai :",b,"Binary :",format(b,"08b"))
print ("\n---------- --------(|)")
print ("Nilai :",c,"Binary :",format(c,"08b"))


# Bitwise And (&)
c = a & b
print ("\n==========And=========")
print ("Nilai :",a,"Binary :",format(a,"08b"))
print ("Nilai :",b,"Binary :",format(b,"08b"))
print ("\n-------------------(&)")
print ("Nilai :",c,"Binary :",format(c,"08b"))


# Bitwise XOR (|)
c = a ^ b
print ("\n==========XOR=========")
print ("Nilai :",a,"Binary :",format(a,"08b"))
print ("Nilai :",b,"Binary :",format(b,"08b"))
print ("\n------------------(^)")
print ("Nilai :",c,"Binary :",format(c,"08b"))


# Bitwise Not (~)
c = ~a
print ("\n==========NOT=========")
print ("Nilai :",a,"Binary :",format(a,"08b"))
print ("\n------------------(~)")
print ("Nilai :",c,"Binary :",format(c,"08b"))

d = 0b00001001
e = 0b11111111
print ("Nilai :",d^e,"Binary :",format(d^e,"08b"))


# Shifting
# # Shifting Right (>>)
c = a >> 1
print ("\n==========>>=========")
print ("Nilai :",a,"Binary :",format(a,"08b"))

print ("\n------------------(|)")
print ("Nilai :",c,"Binary :",format(c,"08b"))


# # Shifting Left (<<)
c = a << 1
print ("\n==========>>=========")
print ("Nilai :",a,"Binary :",format(a,"08b"))

print ("\n------------------(|)")
print ("Nilai :",c,"Binary :",format(c,"08b"))