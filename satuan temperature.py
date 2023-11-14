# Latihan satuan Temperature

print ("=" * 45)
print ("\n\tPROGRAM KONVERSI TEMPERATURE\n")
print ("=" * 45)

# Celcius Ke Reamur 

print (" ")

celcius = float(input("Masukkan Suhu Dalam Celcius : "))
print ("Suhu Adalah : ",celcius, "Celcius")

reamur = (4 / 5) * celcius 
print ("Suhu Dalam Reamur Adalah : ",reamur)


# Celcius ke Fahrenheit 

print (" ")

celcius = float(input("Masukkan Suhu Dalam Celcius : "))
print ("Suhu Adalah : ",celcius ,"Celcius")

fahrenheit = ((9 / 5) * celcius) + 32  
print ("Suhu Dalam Fahrenheit Adalah : ",fahrenheit) 


# Celcius Ke Kelvin

print (" ")

celcius = float(input("Masukkan Suhu Dalam Celcius : "))
print ("Suhu Adalah : ",celcius ,"Celcius")

kelvin = celcius + 273 
print ("Suhu Dalam Kelvin Adalah : ",kelvin) 


# Fahrenheit Ke kelvin

print (" ")

fahrenheit = float(input("Masukkan Suhu Dalam Fahrenheit : "))
print ("Suhu Adalah : ",fahrenheit,"Fahrenheit")

celcius = (5 / 9 * (fahrenheit - 32))
kelvin = celcius + 273
print ("Suhu Dalam Kelvin Adalah : ",kelvin, "Kelvin")

# Kelvin Ke Fahrenheit

print (" ")

kelvin = float(input("Masukkan Suhu Dalam Kelvin : "))
print ("Suhu Adalah : ",kelvin, "Kelvin")

celcius = kelvin - 273
fahrenheit = ((9 / 5) * celcius) - 32
print ("Suhu Dalam Fahrenheit Adalah : ",fahrenheit, "Fahrenheit")