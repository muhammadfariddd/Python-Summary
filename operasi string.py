# Operasi dann Manipulasi String

# 1. Menyambung String (concatenate)

nama_depan = "Monkey"
nama_tengah = "D"
nama_belakang = "Luffy"

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator Untuk String

# Mengecek apakah ada komponen char atau string di string

check = "d"
status = check in nama_lengkap
print(check + " ada di " + nama_lengkap + " = " + str(status))

check = "D"
status = check in nama_lengkap
print(check + " ada di " + nama_lengkap + " = " + str(status))

check = "d"
status = check not in nama_lengkap
print(check + " tidak ada di " + nama_lengkap + " = " + str(status))

# Mengulang string
print("wk" * 10)
print(15 * "wk")

# Indexing
print("index ke-0    : " + nama_lengkap[0])
print("index ke-8    : " + nama_lengkap[8])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[3:7] : " + nama_lengkap[3:7])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2])

# Paling kecil
print("Paling kecil : " + min(nama_lengkap))

# Paling besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 121
print("Char untuk ASCII 121 adalah : " + chr(data))

# 4. Operator dalam bentuk method

data = "mina mina simahawa"
jumlah = data.count("a")
print("Jumlah a pada " + data + " = " + str(jumlah))
