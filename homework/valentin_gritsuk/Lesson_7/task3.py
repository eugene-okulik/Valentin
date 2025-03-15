def print_addition(*args):
    for arg in args:
        print(int(arg[arg.index(':') + 2:]) + 10)


res1 = 'результат операции: 42'
res2 = 'результат операции: 54'
res3 = 'результат работы программы: 209'
res4 = 'результат: 2'
print_addition(res1, res2, res3, res4)
