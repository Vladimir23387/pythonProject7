year_pushkin = int(input("Введите год рождения А.С. Пушкина: "))

if year_pushkin == 1799:
    day_pushkin = int(input("Введите день рождения А.С. Пушкина: "))
    if day_pushkin == 6:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")