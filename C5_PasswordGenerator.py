#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Password
password_list = []
for i in range(0, nr_letters):
  #char=random.choice(letters)
  #password_list=password_list+ [char]
  #print(password_list)
  password_list.append(random.choice(letters))

for j in range(0, nr_symbols):
  password_list+=random.choice(symbols)

for k in range(0, nr_numbers):
  password_list+=random.choice(numbers)
#print(password_list)

#Shuffle the list
random.shuffle(password_list)
#print(f"{password_list} \n \n")

#Print list to String
password=""
for i in password_list:
  password= password+i

print("f your password is : {password} ")



"""
# Easy Password
password = ""
for i in range(0, nr_letters):
  #password+=random.choice(letters)
  random_char =random.choice(letters)
  password=password+random_char
print(password)
# password = password+random.choice(letters)


for i in range(0,nr_numbers):
  random_num = random.choice(numbers)
  password=password+random_num
  print(password)

for j in range(0,nr_symbols):
  random_sym = random.choice(symbols)
  password = password+random_sym
  print(password)

"""
