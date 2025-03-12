res1 = 'результат операции: 42'
res2 = 'результат операции: 514'
res3 = 'результат работы программы: 9'
print(int(res1[res1.index(':') + 2:]) + 10)
print(int(res2[res2.index(':') + 2:]) + 10)
print(int(res3[res3.index(':') + 2:]) + 10)
