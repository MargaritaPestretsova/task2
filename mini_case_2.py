print('Вы любитите заниматься спортом?')
answer = input('Ваш ответ: ')
if answer.lower() == 'да':
    print('Сколько раз в неделю Вы занимаетесь спортом?')
    answer1 = int(input(''))
    if answer1 == 1:
        print('Неплохо, но могло быть и лучше')
    elif answer1>=2 and answer1<=3:
        print('Вы молодец, продолжайте в том же духе!!')
    else:
        print('Вы настоящий спортсмен!!')
elif answer.lower() == 'нет':
    print('Почему вы не занимаетесь спортом? Выберите ваш вариант ответа: а.Нет времени б.Лень в.Не нравится г.По состоянию здоровья')
    answer11 = input('Выберите ваш вариант ответа: ')
    if answer11.lower() == 'а':
        print('Это очень полезное занятие, советуем Вам найти на него время')
    elif answer11.lower() == 'б':
        print('Как говорил Дарвин:"Нет ничего более выносимого, чем безделье." Не ленитесь!')
    elif answer11.lower() == 'в':
        print('Очень жаль')
    else:
        print('Поправляйтесь скорее!!')
else:
    print('Введите "да" или "нет"')
