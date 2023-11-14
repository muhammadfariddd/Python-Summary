data = "Ini Adalah String"
print(data)
print(type(data))

# 1.Cara membuat String

"""
    1.Menggunakan Single Quote '...'
    2.Menggunakan Double Quote "..."
"""

data = 'Menggunakan Single Quote'
print(data)

data = "Menggunakan Double Quote"
print(data)

print("'Halo, Apa Kabar?'")
print('"Halo, Apa Kabar?"')
print("Ini Adalah Hari Jum'at")

# 2.Menggunakan Tanda \

# Membuat Tanda ' Menjadi String
print("Mari Shalat Juma'at")
print("g'day, isn't it?")

# Backslash
print("C:\\Users\\Asus")

# Tab
print("Ucup\tOtong, Jauhan ")
print("Ucup\t\t\tOtong, Semakin Jauhan ")

# Backspace
print("Ucup \bOtong, Jadi Deket")

# Newline
print("Baris Pertama.\nBaris Kedua.")  # LF -> Line Feed -> unix, macos, linux
print("Baris Pertama.\rBaris Kedua.")  # CR -> Carriage Return -> commodore, acorn ,lisp
print("Baris Pertama.\r\nBaris Kedua.")  # CRLF -> Line Feed Carriage Return -> windows


# 3.String Literal atau Raw

# hati-hati
print("C:\new folder")  # akan salah pathnya

# Menggunakan Raw String
print(r"C:\new folder")

# Multilane Literal String
print(
    """
Nama : Farid
Kelas : DA
"""
)

# Multilane Literal String dan Raw
print(
    r"""
Nama : Farid
Kelas : DA\new student
Website : https://muhammadfariddd.github.io/My-Website.
"""
)
