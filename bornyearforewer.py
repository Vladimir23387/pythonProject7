correct_birthyear = 1799

while True:
    answer = input('Назовите год рождения Пушкина: ')
    try:
        answer = int(answer)
        if answer == correct_birthyear:
            print('Верно')
            break
        else:
            print('Неверно')
    except ValueError:
        print('Пожалуйста, введите целое число')
