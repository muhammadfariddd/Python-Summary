## Operasi

# index   0(-3) 1(-2) 2(-1)
data = ["Farid", "Love", "Hesti"]

data_0 = data[0]
print(f"Data pertama adalah  = {data_0}")

data_2 = data[-2]
print(f"Data kedua adalah    = {data_2}")

data_terakhir = data[-1]
print(f"Data terakhir adalah = {data_terakhir}")

# Jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data adalah = {panjang_data}")

## Manipulasi data list

# menambah item pada list sesuai posisi
print(f"Data sebelum diubah = \n{data}")
data.insert(0, "Muhammad")
print(f"Data sesudah diubah = \n{data}")

# menambah data di akhir list
data.append("Nur Anggraini")
print(f"Data diubah lagi    = \n{data}")

# menambah list dengan list
data_baru = ["in", "the", "World"]
data.extend(data_baru)
print(f"data gabungan       = \n{data}")

# merubah data
data[2] = "Like"
print(f"Data diubah jadi    = \n{data}")

# meremove data
data.remove("Nur Anggraini")
print(f"Data remove         = \n{data}")
# data.remove("nur anggraini") --> data akan error karena huruf tidak sesuai

# remove data paling belakang
data_akhir = data.pop()
print(f"remove data akhir   = \n{data} ")
print(data_akhir)
