PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
new_dict = {good.split()[0]: int(good.split()[1].replace('р', '')) for good in PRICE_LIST.split('\n')}
print(new_dict)
