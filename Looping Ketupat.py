# sisi = 5

# count = 1
# for i in range(sisi) :
#     print ("*"*count)
#     count += 1

# print (f"for end\n")

print (" ")
sisi = int(input("Masukkan sisi segitiga yang anda inginkan = ")) 
print (" ")

count = 1

spasi = int(sisi/2)
while True :
    if (count%2) :
        print (" "*spasi + "+"*count)
        count += 1
        spasi -= 1
    else :
        count += 1
        continue
         
    if count > sisi :
        break

sisi = sisi - 1
count = 2

spasi = int(count/2)
while True :
    if (sisi%2) :
        print (" "*spasi + "+"*sisi)
        sisi -= 1
        spasi += 1
    else :
        sisi -= 1
        continue
         
    if sisi < count :
        break

print (" ")



# segitiga = int(input("Masukkan sisi segitiga yang anda inginkan = "))

# if segitiga % 2:
#     segitiga = segitiga
# else :
#     segitiga -= 1

# angka = 1

# while angka < segitiga:
#     print ((angka*"*").center(segitiga))
#     angka += 2

# while angka > 0:
#     print ((angka*"*").center(segitiga))
#     angka -= 2