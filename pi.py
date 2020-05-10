from mnemo_functions import pi_reader
import itertools

pi_length = int(input("Сколько цифр после запятой Вы введете"))
pi_field = int(input("По сколько цифр Вы хотите вводить в одном поле"))
print(pi_field)
print()

# количество полей для ввода
pi_field_num = pi_length // pi_field if (pi_length % pi_field) == 0 else pi_length // pi_field + 1
print(pi_field_num)

# общая строка с введенными ползователями цифрами
pi_user_str = ''

'''
		if user_answer.isdigit():
			user_list.append(int(user_answer))
		elif user_answer == '':
			user_list.append('-')
		else:
			user_list.append(user_answer)

'''

# Пользователь вводит цифры в каждом поле, цифры добавляются оператором + в строку pi_user_list
for field_ in range(1, pi_field_num + 1):
    print(field_)
    if field_ != 1 and field_ == pi_field_num:
        print('last row ', pi_field_num)
        user_answer = input()

        # последняя срока ввода равна количеству цифр остаток количество полей

        pi_input_len = pi_field if pi_length % pi_field == 0 else pi_length % pi_field
        user_answer = user_answer[:pi_input_len]
        pi_user_str += user_answer
        if user_answer == '':
            pi_user_str += '/'


    else:
        user_answer = input()
        if user_answer.isdigit():
            if len(user_answer) > pi_field:
                user_answer = user_answer[:pi_field]

            pi_user_str += user_answer
        elif user_answer == '':
            pi_user_str += '-'
        elif user_answer is None:
            pi_user_str += '/'
        else:
            pi_user_str += user_answer

# Открывается файл с строками числа Пи
'''
pi_reader(num)
    :param num: кол-во знаков Пи
    :return: Пи с количеством знаков n после запятой
'''

# Из файла сохраняется в строку количество знаков после Пи, заданное пользователем
pi_computer_str = pi_reader(pi_length)

# Сохраненная строка из файла сравнивается со строкой пользователя

if pi_computer_str == pi_user_str:
    print("Победа")
else:
    print("Поражение")

for computer_item, user_item in itertools.zip_longest(pi_computer_str, pi_user_str):
    print(f'Результат компьютера: {computer_item}, результат пользователя {user_item}')
