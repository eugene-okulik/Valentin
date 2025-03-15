import sys


def fibo_gen():
    a = 0
    b = 1
    while True:
        yield a
        buf = a
        a = b
        b = buf + b


def print_current_fibo_numb(*args):
    sys.set_int_max_str_digits(1000000)
    for arg in args:
        gen_fun_obj = fibo_gen()
        count = 1
        while True:
            fibo_numb = next(gen_fun_obj)
            if count == arg:
                print(f'{arg}-е число Фибоначчи = {fibo_numb}')
                break
            count += 1


print_current_fibo_numb( 5, 200, 1000, 100000)