import random


number = random.randint(1, 10)
print('Я хочу сыграть с вами в игру. Угадайте число, которое я загадал')
while True:
    input_number = int(input())
    if number != input_number:
        print('попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
