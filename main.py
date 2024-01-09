name = input("Hi! Please enter your name:")
age = input(f'Welcome {name}! Please enter your age:')
age = int(age)
if age < 15:
  print(f'{age} I don\'t even remember being that young...')
elif 15<=age<18:
  print(f'"Ah, {age}! Being a teen, those were the days..."')
elif 18<=age<55:
  print(f'{age}, amazing!')
elif 55<=age<120:
  print(f'{age} years old, great!')
elif age>120:
  print(f'{age}? What\'s your secret to living so long?')

option = input("How can I help you today?")
option = int(option)
