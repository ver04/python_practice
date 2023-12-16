# Password Generator Project
import random

lock = ('''
       .--------.
      / .------. \
     / /        \ \
     | |        | |
    _| |________| |_
  .' |_|        |_| '.
  '._____ ____ _____.'
  |     .'____'.     |
  '.__.'.'    '.'.__.'
  '.__  |      |  __.'
  |   '.'.____.'.'   |
  '.____'.____.'____.'
  '.________________.'

''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print(lock)
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


password = []

# Generating random letters from list of letters
for number in range(0, nr_letters):
  random_letter_index = random.randint(0, len(letters)-1)
  password.append(letters[random_letter_index])

# Generating random number from list of numbers
for number in range(0, nr_numbers):
  random_number_index = random.randint(0, len(numbers)-1)
  password.append(numbers[random_number_index])

# Generating random symbol from list of symbols
for number in range(0, nr_symbols):
  random_symbol_index = random.randint(0, len(symbols)-1)
  password.append(symbols[random_symbol_index])


# Joining the letters into a single string
print(f"Before shuffle: {''.join(password)}")

# Do the shuffle
random.shuffle(password)
# Create one string of password characters
shuffled_password = ''.join(password)
# Print result
print(f"After shuffle: {shuffled_password}")
