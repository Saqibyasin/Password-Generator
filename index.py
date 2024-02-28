import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input('How many numbers would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like in your password?\n'))

password = []

for letter in range(nr_letters):
    random_char = random.choice(letters)
    password.append(random_char)

for num in range(nr_numbers):
    random_num = random.choice(numbers)
    password.append(random_num)

for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

random.shuffle(password)

final_password=''

for char in password:
    final_password+=char

print(F'Your Password is: {final_password}')
