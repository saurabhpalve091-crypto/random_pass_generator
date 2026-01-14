import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','%','&','*']

print("Welcome to the Password Generator!")

n_letters =int(input("How many letters you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
n_symbol = int(input("How many symbol you want in your password?\n"))

password=""

for i in range(1,n_letters+1):
    char = random.choice(letters)
    password = password + char
print(password)

for m in range(1,n_numbers+1):
    num = random.choice(numbers)
    password = password + num
print(password)

for n in range(1,n_symbol+1):
    symb = random.choice(symbols)
    password = password + symb

print("Your Password is:", password)