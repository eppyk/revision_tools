import random

filepath = 'questions.txt'


print('\n\n\n\nThis script selects random questions for the AWS Solutions Architect exam.\n')
numberofqs = int(input('How many questions do you want to be asked? >>> '))
with open(filepath) as fp:  
   lines = fp.readlines()
   num_lines = len(lines)
   chosen_lines = random.sample(range(1, num_lines), numberofqs)
   print('Make sure your questions.txt file is updated. \nCurrently there is %d questions in the database. \n\n' %(num_lines))
   cnt = 0
   while cnt < numberofqs:
       print(lines[chosen_lines[cnt]])
       cnt += 1


