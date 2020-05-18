'''

  * Project: Mini-Quiz
  * Author: Emmett
  * Date: 17th May
  * Copyright (C) 2020

'''

import time

# -
# Variables
# -

answ_First = '149600000'
answ_Second = '3.14'
answ_Third = '10'
answ_Fourth = 'None'
answ_Fifth = '100'

MAX_QUIZ_XP = 20
quiz_xp = 0

quiz_Question_First = ""
quiz_Question_Second = ""
quiz_Question_Third = ""
quiz_Question_Fourth = ""
quiz_Question_Fifth = ""

# -
# Function
# -

def endQuiz():
	print('\n\n------------- Quiz is over! -------------')
	print('Your name: ', quiz_User, '\nYour XP: ', quiz_xp, '/', MAX_QUIZ_XP)
	print('-----------------------------------------')

	file = open("scores.txt", "w")
	
	file.write('Your name: {0} | Score: {1}/{2}'.format(quiz_User, quiz_xp, MAX_QUIZ_XP))
	file.close()

# Input user name
quiz_User = input('Enter your name: ')

if len(quiz_User) < 6:
	raise ValueError('Name is too short! Name must containt 6 or greater than 6 letters.')

print('Okay, ', quiz_User, ' good luck.\n\n')

# -
# Questions
# -

print('How far is the sun from the earth?')
quiz_Question_First = input('Answer: ')

quizStarted = 1

# 1
if answ_First not in quiz_Question_First:
	print('Incorrect answer. XP: -5')
	quiz_xp -= 5
	
	time.sleep(1)

	print('\n\nWhat a decimal of π?')
	quiz_Question_Second = input('Answer: ')

else:
	print('Correct answer. XP: +5\n\n')
	quiz_xp += 5

	time.sleep(1)

	print('\n\nWhat a decimal of π?')
	quiz_Question_Second = input('Answer: ')

# 2
if answ_Second not in quiz_Question_Second:
	print('Incorrect answer. XP: -5')
	quiz_xp -= 5

	time.sleep(1)

	print('\n\nA stick and a ball together cost 110 euros. A stick costs 100 euros more than a ball. How much does a ball cost?')
	quiz_Question_Third = input('Answer: ')

else:
	print('Correct answer. XP: +5')
	quiz_xp += 5

	print('\n\nA stick and a ball together cost 110 euros. A stick costs 100 euros more than a ball. How much does a ball cost?')
	quiz_Question_Third = input('Answer: ')

# 3
if answ_Third not in quiz_Question_Third:
	print('Incorrect answer. XP: -5')
	quiz_xp -= 5

	time.sleep(1)

	print('\n\nWhat place are you in if you cross the last person in the race?')
	quiz_Question_Fourth = input('Answer: ')

else:
	print('Correct answer. XP: +5\n\n')
	quiz_xp += 5

	print('\n\nWhat place are you in if you cross the last person in the race?')
	quiz_Question_Fourth = input('Answer: ')

# 4
if answ_Fourth not in quiz_Question_Fourth:
	print('Incorrect answer. XP: -5')
	quiz_xp -= 5

	time.sleep(1)

	print('Five minutes will take 5 machines to make 5 badges. How long would it take for 100 machines to make 100 badges?')
	quiz_Question_Fifth = input('Answer: ')

else:
	print('Correct answer. XP: +5\n\n')
	quiz_xp += 5

	print('Five minutes will take 5 machines to make 5 badges. How long would it take for 100 machines to make 100 badges?')
	quiz_Question_Fifth = input('Answer: ')

# End quiz
if answ_Fifth not in quiz_Question_Fifth:
	print('Incorrect answer. XP: -5')
	quiz_xp -= 5

	time.sleep(1)

	endQuiz()

else:
	print('Correct answer. XP: +5')

	endQuiz()
