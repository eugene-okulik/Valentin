class Flowers:

    def __init__(self, name, freshness, color, stem_length, cost, live_time_days):
        self.freshness = freshness
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.live_time_days = live_time_days
        self.avr_live_time = live_time_days * freshness / 100


class Rose(Flowers):

    def __init__(self, name, freshness, color, stem_length, cost, live_time_days, are_thorn):
        super().__init__(name, freshness, color, stem_length, cost, live_time_days)
        self.are_thorn = are_thorn


class Lupin(Flowers):

    def __init__(self, name, freshness, color, stem_length, cost, live_time_days, poison_is_in):
        super().__init__(name, freshness, color, stem_length, cost, live_time_days)
        self.poison_is_in = poison_is_in


class Orchid(Flowers):

    def __init__(self, name, freshness, color, stem_length, cost, live_time_days, acid_is_in):
        super().__init__(name, freshness, color, stem_length, cost, live_time_days)
        self.acid_is_in = acid_is_in


class Bouquet:
    def __init__(self):
        self.flowers = []  # Список для хранения цветов в букете

    def add_flower(self, *args):
        self.flowers.extend(args)

    def print_full_cost(self):
        print(f'Цена букета - {sum(flower.cost for flower in self.flowers)} руб')

    def print_avr_live_time(self):
        print(f'Среднее время жизни букета - '
              f'{sum(flower.live_time_days for flower in self.flowers) / len(self.flowers)} дней')

    def print_find_by_avr_live_time(self, days):
        print(f'\nПоиск цветка по среднему времени жизни: {days}')
        result = [flower.name for flower in self.flowers if flower.avr_live_time == days]
        if result:
            for name in result:
                print(name)
        else:
            print('Такого цветка здесь нет')

    def sort_by_freshness(self):
        print('\nОтсортировано по свежести')
        self.flowers.sort(key=lambda obj: obj.freshness)

    def sort_by_cost(self):
        print('\nОтсортировано по стоимости')
        self.flowers.sort(key=lambda obj: obj.cost)

    def sort_by_stem_len(self):
        print('\nОтсортировано по длине стебля')
        self.flowers.sort(key=lambda obj: obj.stem_length)

    def sort_by_color(self):
        print('\nОтсортировано по цвету')
        self.flowers.sort(key=lambda obj: obj.color)

    def __str__(self):
        bouquet = ('Ваш букет\n')
        for flower in self.flowers:
            bouquet += (f'{flower.name}: длина стебля - {flower.stem_length}, '
                        f'цена - {flower.cost}, свежесть - {flower.freshness}, цвет - {flower.color}\n')
        return bouquet


red_rose = Rose(
    'Красная роза', 100, 'красный', 75, 250, 2, True
)
yellow_orchid = Orchid(
    'Красная орхидея', 80, 'красный', 56, 180, 4, False
)
lupin = Lupin(
    'Желтый тюльпан', 85, 'желтый', 64, 195, 3, False
)
bouquet = Bouquet()
bouquet.add_flower(red_rose, yellow_orchid, lupin)
print(bouquet)
bouquet.print_full_cost()
bouquet.print_avr_live_time()
bouquet.print_find_by_avr_live_time(3)
print(f'времена жизни наших цветков: {red_rose.avr_live_time} {yellow_orchid.avr_live_time} {lupin.avr_live_time}')
bouquet.print_find_by_avr_live_time(2.55)
bouquet.sort_by_freshness()
print(bouquet)
bouquet.sort_by_cost()
print(bouquet)
bouquet.sort_by_color()
print(bouquet)
bouquet.sort_by_stem_len()
print(bouquet)
