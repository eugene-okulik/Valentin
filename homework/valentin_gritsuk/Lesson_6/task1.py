text = ("Etiam tincidunt neque erat, quis "
        "molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
fin_text = ''
for word in words:
    if word.endswith(','):
        fin_text += word.replace(',','ing, ')
    elif word.endswith('.'):
        fin_text += word.replace('.','ing. ')
    else: fin_text += word + 'ing '
print(fin_text.rstrip())
