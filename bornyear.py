pushkin_birthyear = 1799
pushkin_birthyear = int(pushkin_birthyear) # приведение к целочисленному виду

answer = 0
answer = input('Назовите год рождения Пушкина ')
answer = int(answer)

if answer == pushkin_birthyear:
    print('Верно')
else:
    print('Неверно')

