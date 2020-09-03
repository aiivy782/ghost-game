from random import randint
import colorama
import os

os.system('figlet "GHOST GAME"')
feeling_brave = True
score = 0

while feeling_brave: 
	ghost_door = randint(1, 3)
	print('\033[34mYou have tree doors ahead.\033[0m')
	print('\033[1mA ghost behind one.\033[0m')
	print('\033[1mWhich door do you open?\033[0m')
	door = input('\033[34m1\033[0m, \033[32m2\033[0m or \033[31m3\033[0m?')
	door_num = int(door)

	if door_num == ghost_door:
		print('\033[1m\033[33mOH SHIT! GHOST!!!\033[0m')
		feeling_brave = False
	else:
		print('Oh, there is not any ghosts.')
		print('\033[4mNext room.\033[0m')
		score = score + 1

print('\033[1mRun away!\033[0m')
print('Game over, you scored', score)