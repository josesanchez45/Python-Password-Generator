#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# easyPassword = ""
# for char in range(1, nr_letters + 1):
#     easyPassword += random.choice(letters)
# for symbol in range(1, nr_symbols + 1):
#     easyPassword += random.choice(symbols)
# for number in range(1, nr_numbers + 1):
#     easyPassword += random.choice(numbers)

# print(f"Your random password is : {easyPassword}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
newList = []
hardPassword = ""
for char in range(1, nr_letters + 1):
    newList.append( random.choice(letters))
for symbol in range(1, nr_symbols + 1):
    newList.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
    newList.append(random.choice(numbers))

random.shuffle(newList)
for character in newList:
    hardPassword += character

print(f"Your new password is: {hardPassword}")