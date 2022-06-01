from random import *

#Вступление

print('Добро пожаловать в числовую угадайку! Напишите предел загадываемого числа: от 1 до ...?')
limit = input()

#Защита от дурака
 
def is_valid(num):
  if num.isdigit() and limit.isdigit() and 1 <= int(num) <= int(limit):
    return True
  else:
    return False
# Сама игра

def game():
    n = randint(1, int(limit))
    counter = 0
    while True:
        num = input('Введите целое число от 1 до 100: ' + '\n')
        if is_valid(num):
            num = int(num)
            if num == n:
                counter += 1
                print("Вы угадали, поздравляем!")
                break
            elif num > n:
                counter += 1
                print("Ваше число больше загаданного, попробуйте еще разок")
                continue
            else:
                counter += 1
                print("Ваше число меньше загаданного, попробуйте еще разок")
                continue
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
    print('Количество попыток: ', counter)
    print('Спасибо, что играли в числовую угадайку. Хотите сыграть еще раз?(Да/Нет)')
    answer = input()
    if answer == 'Да':
        game()
    else:
        print('Заходите еще!')
game()
