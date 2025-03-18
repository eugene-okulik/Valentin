def decor(func):

    def wrapper(first, second, operation = None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return first / second


first, second = map(int, input('Введите два числа через пробел: ').split())
print(calc(first, second))
