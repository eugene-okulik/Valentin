def choosing_high_temp(x):  # high temp is temp > 28
    return list(filter(lambda i: i > 28, x))


temperatures = [20, 15, 32, 34, 21, 19, 25, 27,
                30, 32, 34, 30, 29, 25, 27, 22, 2,
                23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
high_temperature = choosing_high_temp(temperatures)
print(f'Самая высокая температура = {max(high_temperature)}, самая низкая температура = {min(high_temperature)}')
