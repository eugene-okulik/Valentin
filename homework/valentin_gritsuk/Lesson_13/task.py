import os
import datetime
import locale


def read_file(path):
    with open(path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(data_path)

for data_line in read_file(data_path):
    time = (data_line[3: (data_line.index('распечатать') - 3)])
    time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
    if data_line[0] == '1':
        print(time + datetime.timedelta(days=7))
    elif data_line[0] == '2':
        locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')
        print(time.strftime("%A"))
    elif data_line[0] == '3':
        print((datetime.datetime.now() - time).days)
