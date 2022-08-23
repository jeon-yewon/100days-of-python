#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Eazy Level - Order not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# pw_letters=""
# pw_symbols=""
# pw_numbers=""
# for i in range(0, nr_letters):
#   rand_index = random.randint(0,len(letters)-1)
#   pw_letters += letters[rand_index]
#   # print(i, pw_letters)

# for i in range(0, nr_symbols):
#   rand_index = random.randint(0,len(symbols)-1)
#   pw_symbols += symbols[rand_index]
#   # print(i, pw_symbols)

# for i in range(0, nr_numbers):
#   rand_index = random.randint(0,len(numbers)-1)
#   pw_numbers += numbers[rand_index]
#   # print(i, pw_numbers)

# print(f"Your password is : {pw_letters + pw_symbols + pw_numbers}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
temp_list = []
for i in range(0, nr_letters):
  temp_list += [random.choice(letters)]
  # print(temp_list)
for i in range(0, nr_symbols):
  temp_list += [random.choice(symbols)]
  # print(temp_list)
for i in range(0, nr_numbers):
  temp_list += [random.choice(numbers)]
  # print(temp_list)

pw_list = random.sample(temp_list, len(temp_list))
# print(temp_list)
# print(pw_list)

password = ""
for char in pw_list:
  password += char

print(f"Your password is {password}")

# # random.sample() test
# sample_list_1 = random.sample(temp_list, len(temp_list))
# sample_list_2 = random.sample(temp_list, len(temp_list)-1)
# print(sample_list_1)
# print(sample_list_2)