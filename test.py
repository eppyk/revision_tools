import random

filepath = 'questions.txt'


print('\n\n\n\nThis script selects 5 random questions for the AWS Solutions Architect exam.\n')

with open(filepath) as fp:  
   lines = fp.readlines()
   num_lines = len(lines)
   print('Make sure your questions.txt file is updated. \n\nCurrently there is %d questions in the database. \n\n\n\n' %(num_lines))
   cnt = 0
   while cnt < 5:
       randomnum = random.randint(1, num_lines-1)
       print(lines[randomnum])
       cnt += 1
       randomnum = random.randint(1, num_lines)


