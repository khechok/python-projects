import random
top_of_range = input('Type a number: ')

if top_of_range.isdigit():
   top_of_range = int(top_of_range)

   if top_of_range <= 0:
      print('please type a number greater than 0')
      quit()
else:
   print('please type a number next time!')
   quit()

random_number = random.randint(0,top_of_range)
print(random_number)
guesses = 0

while True:
   guesses += 1
   user_number = input('Guess a number: ')
   if user_number.isdigit():
      user_number = int(user_number)

   else:
      print('please a type a number')
      continue

   if user_number == random_number:
      print('You got it right!')
      break
   else:
      print('You got it wrong!')

print('You got it in', guesses 'guesses')
