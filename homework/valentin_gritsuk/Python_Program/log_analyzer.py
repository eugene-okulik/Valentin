import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Указывается папка с логами")
parser.add_argument("--text", required=True, help="Текст для поиска в логах")
args = parser.parse_args()


def print_context(lines, line, row_counter):
    words = line.split()
    for index, word in enumerate(words):
        if args.text.split()[0] == word:
            start = max(0, index - 5)
            real_start = index - 5
        if args.text.split()[-1] == word:
            end = min(len(words), index + 6)
            real_end = index + 5
    context = ' '.join(words[start:end])
    if lines[row_counter - 1]: # Если в найденной строке до искомого текста меньше 5 слов, берём слова из пред. строки
        if real_start < 0:
            words_add_st = lines[row_counter - 1].split()
            context_add_st = ' '.join(words_add_st[len(words_add_st) + real_start - 1:])
            context = context_add_st + context
    if  lines[row_counter + 1]: # Если в найденной строке после искомого текста больше 5 слов, берём из след. строки
        if real_end > len(words):
            words_add_end = lines[row_counter + 1].split()
            context_add_end = ' '.join(words_add_end[:real_end - len(words)])
            context = context + context_add_end
    print(f'... {context} ...\n')


contents = os.listdir(args.directory)
for file in contents:
    row_counter = 1
    path = os.path.join(args.directory, file)
    with open(path, 'r') as data_file:
        lines = data_file.readlines()
        for line in lines:
            if args.text in line:
                print(f'Указанный текст находится в файле "{file}" в строке №{row_counter}')
                print_context(lines, line,  row_counter)
            row_counter += 1
