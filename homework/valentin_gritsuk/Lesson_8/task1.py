import random

salary = int(input("Укажи свою зарплату: "))
bonus = random.choice([True, False])
if bonus:
    print(f"{salary}, {bonus} - '${int(salary * (random.uniform(1.0, 10.0)))}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")