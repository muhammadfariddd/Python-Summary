# Operator dalam bentuk method 

## Merubah case dari string 


# Merubah semua ke upper case 
normal = "bro!"
print ("normal = " + normal)
print ("upper = " + normal.upper())


# Merubah semua ke lower case 
normal = "aKu KecE AbieezZzZZZZZ"
print ("normal = " + normal)
print ("lower = " + normal.lower())


## Pengecekan dengan isX method

# Contoh pengecekan lower case  
sist = "ssttt"
apakah_lower = sist.islower() # hasilnya boolean
print (sist + " is lower = " + str(apakah_lower))

# Contoh pengecekan lower case  
apakah_upper = sist.isupper() # hasilnya boolean
print (sist + " is upper = " + str(apakah_lower))

# Contoh pengecekan jika semuanya adalah huruf 
apakah_alpha = sist.isalpha()
print (sist + " is alpha = " + str(apakah_alpha))

# Contoh pengecekan huruf dan angka
apakah_alnum = sist.isalnum()
print (sist + " is alnum = " + str(apakah_alnum))

# Contoh pengecekan angka saja  
apakah_decimal = sist.isdecimal()
print (sist + " is decimal = " + str(apakah_decimal))

# Contoh pengecekan spasi, tab, newline \n
apakah_space = sist.isspace()
print (sist + " is space = " + str(apakah_space))

# Contoh pengecekan semua kata dimulai dengan huruf besar   
title = "It Is Okay Not To Be Orkay"
is_title = title.istitle()
print (title + "is title = " + str(is_title))

# Cek komponen startswith() dan endswith()
ceck_start =  "Muhammad Farid".startswith("Muhammad")
print ("start = " + str(ceck_start))

ceck_end =  "Muhammad Farid".endswith("Farid")
print ("end = " + str(ceck_end))

# Penggabungan komponen join() split()
var = ['aku','sayang','kamu']
gabung = ','.join(var)
print (var)
print (gabung)

gabung = ' '.join(var)
print (gabung)

gabung = ' ehm '.join(var)
print (gabung)

gabungan = "akuehmsayangehmkamu"
print (gabungan.split('ehm'))


# Alokasi karakter rjust(), ljust(), center() 

kanan = "kanan".rjust(10)
print ("'"+kanan+"'")

kiri = "kiri".ljust(10)
print ("'"+kiri+"'")

tengah = " tengah ".center(20,"=")
print ("="+tengah+"=")

# Kebalikannya -> strip ()
tengah =  tengah.strip("=") # Menghilangkan tanda =
print (tengah)