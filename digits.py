'''NUMBER MEMORY'''

import random
import sys
import itertools

print("Hello, I am memory app")
print("I can test your number memory ")

wins = 0
loose = 0
results = 0

while True:
# Пользователь задает параметры
# Пользователь вводит количество чисел

	# параметры - до 10 000
	num_list_length = 100001
	while (num_list_length > 10000):
		try:
			num_list_length = int(input("Input length of the number list: "))
			if num_list_length > 10000:
				input_help = input("Input 'help' to see the parameters")
				if input_help == 'help':
					print('Max number is 10000')
		except:
			print("Вы ввели не число")



# Пользователь вводит количество цифр в числе
# If the loop must stop when at least one of the variables is >= z, then you must use and to connect the conditions

	num_of_digits_in_number = 0
	while (num_of_digits_in_number != 2) and (num_of_digits_in_number != 1):
		try:
			num_of_digits_in_number = int(input("Input length of one number - 1 or 2"))
		except:
			print("Вы ввели не число")

	#Генерация списка computer_list длины n
	#с рандомно определенными m-значными числами
	if num_of_digits_in_number == 1:
		computer_list = [random.randint(0,9) for x in range(num_list_length)]
	if num_of_digits_in_number == 2:
		computer_list = [random.randint(10,99) for x in range(num_list_length)]

	# Вывод списка пользователю
	print(computer_list)

	# n раз
	# Пользователь вводит ответ
	user_list = []
	for user_input in range(num_list_length):
		# Ответ добавляется в список user_list
		user_answer = input('Введите число: ')
		print(user_answer)
		if user_answer.isdigit():
			user_list.append(int(user_answer))
		elif user_answer == '':
			user_list.append('-')
		else:
			user_list.append(user_answer)


# Списи computer_list и user_list сравниваются
	# True
	if computer_list==user_list:
		print("Вы победили")
		wins += 1
		results += 1
		print(f"Вcего побед: {wins}")
		print(f"Вcего поражений: {loose}")
		print(f"Общее количество: {results}")
	# False
	else:
		print("Вы проиграли")
		loose += 1
		results += 1
		print(f"Вcего побед: {wins}")
		print(f"Вcего поражений: {loose}")
		print(f"Общее количество: {results}")

# Результаты
	for computer_item, user_item in itertools.zip_longest(computer_list, user_list, fillvalue=0):
		print(f"Результаты компьютера: {computer_item}, результаты пользователя: {user_item}")

	# Еще раз?
	one_mote_time = input("Ещё раз? (y/n)")
	if one_mote_time == 'y':
		continue
	else:
		sys.exit()