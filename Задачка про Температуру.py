def temperature(dg, sc):
    if sc == 'f':
        dg = (dg - 32) / 1.8
        print("Ваша температура по Цельсию - " + str(dg))
    elif sc == 'c':
        dg = dg * 1.8 + 32
        print("Ваша температура по Фаренгейту - " + str(dg))


degree = int(input("Введите вашу температуру:"))
scale = input("Введите шкалу измерения:")

temperature(degree, scale)