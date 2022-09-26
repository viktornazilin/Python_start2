song = input()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
parts = song.split()
itog = list()
for item in parts:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    itog.append(k)
if len(set(itog)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')