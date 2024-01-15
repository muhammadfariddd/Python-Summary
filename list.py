# === List ===

# Int 
data_int = [1, 2, 3]
print (data_int)

# String 
data_str = ["Farid", "Hesti"]
print (data_str)

# Boolean 
data_bool = [True, False]
print (data_bool)

# Range 
data_range = list(range(0, 10)) 
print (data_range)

# Use For 
list_pake_for = [i for i in range(0, 10)] 
print (list_pake_for)

# Pangkat 
list_pake_for = [i**2 for i in range(0, 10)] 
print (list_pake_for)

# remove number 5 
list_pake_for_if = [i for i in range(0, 10) if (i != 5)] 
print (list_pake_for_if)

# Angka Genap 
angka_genap = [i for i in range(0, 10) if (i % 2 == 0)] 
print (angka_genap)

# Angka Ganjil 
angka_ganjil = [i for i in range(0, 10) if (i % 2 != 0)] 
print (angka_ganjil)