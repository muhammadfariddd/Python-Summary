# Membuat Area Rentang Dari Angka
# +++++3------10++++++
inputUser =float(input("Masukkan Angka Bernilai\nKurang Dari 3\nAtau\nLebih Dari 10\n: "))

# Memeriksa Angka Kurang Dari 3 
angkaKurangDari = (inputUser < 3)
print ("Kurang Dari 3 = ",angkaKurangDari)

# Memeriksa Angka Lebih Dari 10 
angkaLebihDari = (inputUser > 10)
print ("Lebih Dari 10 = ",angkaLebihDari)

isCorrect = angkaKurangDari or angkaLebihDari
print ("Angka Yang Anda Masukkan = ",isCorrect)

print ("\n",10 * "=","\n")

# Kasus Irisan
# Memeriksa Angka kurang Dari 3 Atau Lebih Dari 10 
# (------3++++++10------)
inputUser =float(input("Masukkan Angka Bernilai\nLebih Dari 3\nAtau\nKurang Dari 10\n: "))

# Lebih Dari 3
isLebihDari = (inputUser > 3)
print ("Lebih Dari 3 = ",isLebihDari)

# Kurang Dari 10
isKurangDari = (inputUser < 10)
print ("Lebih Dari 10 = ",isKurangDari)


isCorrect = isKurangDari and isLebihDari
print ("Angka Yang Anda Masukkan = ",isCorrect)


# Exercise 1
inputUser = float(input("\nMasukkan Angka Bernilai\nLebih dari 0\nAtau\nKurang Dari 5\nDan\nLebih Dari 8\nAtau\nKurang Dari 11 = "))

antaraNolDan5 = (inputUser > 0 and inputUser < 5)
print ("Nilai > 0 Dan < 5 = ",antaraNolDan5)

antaraNo8Dan11 = (inputUser > 8 and inputUser < 11 )
print ("Nilai > 8 Dan < 11 = ",antaraNo8Dan11)

answer = antaraNolDan5 or antaraNo8Dan11
print ("Nilai Antara 0 Hingga 5 Atau Antara 8 Hingga 11 = ",answer)

print (" ")

# Exercise 2
inputUser = float(input("\nMasukkan Angka Bernilai\nKurang dari 0\nDanlo\nLebih Dari 5\nAtau\nKurang Dari 8\nDan\nLebih Dari 11 = "))

a = (inputUser < 0 or inputUser > 5 )
print ("Nilai < 0 atau > 5 = ",a)

b = (inputUser < 8 or inputUser > 11)
print ("Nilai < 8 atau > 11 = ",b)

answer = a and b
print ("Nilai Kurang Dari 0 Dan Antara 5 Hingga 8 Dan Lebih Dari 11 = ",answer)