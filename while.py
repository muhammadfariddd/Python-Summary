# While Loop

# while kondisi :
#     aksi ini
#     aksi itu

# print (20*"=")
# print (" WHILE LOOP ".center(20,"="))
# print (20*"=")

# angka = 0
# print (f"angka sekarang adalah : {angka}".capitalize())

# while angka <= 5 :
#     angka += 1
#     print (f"angka sekarang adalah : {angka}".capitalize())
#     print ("Hai Hesti")



# exercise 1
# name = input("Enter your name : ")

# while name == "":
#     print("You did not enter your name"+"\n")
#     name = input("Enter your name : ")


# print(f"Your name is {name}")


# exercise 2
# age = int(input("Enter your age : "))

# while age < 0:
#     print("Age cannot be negative"+"\n")
#     age = int(input("Enter your age : "))

# print(f"Your age is {age} years")


# exercise 3
# hobby = input("Enter your favorite hobby (q to quit) : ")

# while not hobby == "q" and not hobby == "Q":
#     print(f"Your hobby is {hobby}" + "\n")
#     hobby = input("Enter your favorite hobby again: (q to quit) :")

# print("Good bye")



# exercise 4
num = int(input("Enter a number between 1 - 10 : "))

while num < 1 or num > 10:
    print(f"{num} is not valid" + "\n")
    num = int(input("Enter a number between 1 - 10 : "))

print(f"The number you picked is {num}")