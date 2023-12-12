# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass

    print(angka)


# continue

angka = 0

print (f"Angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"Angka sekarang adalah {angka}") #aksi 1
    if angka == 3:
        print("Nyenyenye")
        continue #akan membuat loop loncat ke step selanjutnya

    print("Hallo Hesti") # aksi 2

print("Akhir program")



