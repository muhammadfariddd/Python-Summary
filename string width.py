data_nama = "Muhammad Farid"
data_umur = 19
data_tinggi = 160.0
data_no_sepatu = 42

data_string = "\n" + 5 * "=" + " Data String " + 5 * "="


# String Standard
data_lengkap = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor Sepatu = {data_no_sepatu}"

print(data_string)
print(data_lengkap)


# String Multiline (dengan menggunakan enter, newsline, \n)
data_lengkap = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nNomor Sepatu = {data_no_sepatu}"

print(data_string)
print(data_lengkap)


# String Multiline (kutip triplets)
data_lengkap = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Ukuran Sepatu = {data_no_sepatu}
"""

print(data_string)
print(data_lengkap)


# Mengatur Lebar
data_lengkap = f"""Nama      = {data_nama:>5}
Umur      = {data_umur:>5}
Tinggi    = {data_tinggi:>5}
No.Sepatu = {data_no_sepatu:>5}
"""
print(data_string)
print(data_lengkap)
