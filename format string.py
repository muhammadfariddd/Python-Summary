# Format string 

tengah = " Format String ".center(30,"=")
print ("\n="+tengah+"=\n")


# Contoh generic 
# String 
nama = "ucup"
format_str = f"Hello {nama}"

print (format_str)


# Angka 
angka = 2005.5
format_angka = f"Angka = {angka}"

print (format_angka)


# Boolean 
boolean = True
format_bool = f"Boolean = {boolean}"

print (format_bool)


# Bilangan Bulat 
bilangan_bulat = 15 
format_angka = f"Bilangan Bulat = {bilangan_bulat:d}"

print (format_angka)


# Bilangan Dengan Ordo Ribuan 
angka = 2000
format_str = f"Ribuan = {angka:,}"
print (format_str)


# Bilangan Desimal
desimal = 2005.54321
format_str = f"Desimal = {desimal:.3f}"
print (format_str)


# Menampilkan Leadingg Zero 
desimal = 2005.54321
format_str = f"Desimal = {desimal:010.3f}"
print (format_str)


# Menampilkan Tanda + atau -
angka_minus = -10
angka_plus = 10.2345
format_minus = f"Minus = {angka_minus:+d}"
format_plus = f"Plus = {angka_plus:+.2f}"


print (format_minus)
print (format_plus)


# Format Persen 
persen = 0.045
format_persen = f"Persen = {persen:.2%}"
print (format_persen)


# Operasi Aritmatika Didalam Placeholder
harga = 50000
jumlah = 1
harga_total = f"Harga Total = Rp. {harga*jumlah:,}"
print (harga_total)


# Format Angka Lain (Binary, Octal, Hexadecimal)
angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hexadecimal = {hex(angka)}"

print (format_binary)
print (format_octal)
print (format_hex)