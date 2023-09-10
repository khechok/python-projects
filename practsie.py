# building a simple python quize projects
print('welcome to Quiz game!')
answer = input('Do you wanna play quiz?')
if answer.lower()=='yes':
   print('lets play!')
   score=0
else:
   print('come gain next time')
   quit()

answer =input('what is CPU stands for?: ')
if answer.lower()=='central processing unit':
   print(answer + ' is correct answer!')
   score += 1
else:
   print(answer + ' is incorrect!')

answer = input('what is GPU stnads for?: ')
if answer.lower()=='graphical processing unit':
   print(answer + ' is correct answer!')
   score += 1
else:
   print(answer + ' is incorrect answer!')

answer = input('what is aws stands for?: ')
if answer.lower()=='amazone web services' or 'amazone web servcie':
   print(answer + ' is correct answer!')
   score += 1
else:
   print(answer + ' is incorrect answer!')
   quit()

answer = input('what is GCP stands for in cloud concept?: ')
if answer.lower()=='google cloud plateform':
   print(answer + ' is a correct answer')
   score += 1
   quit()
else:
   print(answer + ' is incorrect answer!')

result = 'you have got '+ str(score) + ' correct answer'
print(result)

percentage = 'you have got ' + str((score/4)*100) + " %."
print(percentage)


