
'''def prime_digit(num):
    a = []
    for i in range(num, 0, -1):
        if num % i == 0:
            a.append(i)
    if len(a) == 2:
        return True
    else:
        return False


def first_digit(num):
    n = int(str(abs(num))[0])
    return n


def last_digit(num):
    n = num % 10
    return n


list_of_number = []


for element in range(2095, 19402):
    if prime_digit(element) and first_digit(element) > last_digit(element):
        list_of_number.append(element)


print(len(list_of_number))

list_of_number_2 = []
for i in range(len(list_of_number)):
    if list_of_number[i] % 100 == 21:
        list_of_number_2.append(list_of_number[i])


print(len(list_of_number_2))'''


'''def temperature(dg, sc):
    if sc == 'f':
        dg = (dg - 32) / 1.8
        print("Ваша температура по Цельсию - " + str(dg))
    elif sc == 'c':
        dg = dg * 1.8 + 32
        print("Ваша температура по Фаренгейту - " + str(dg))


degree = int(input("Введите вашу температуру:"))
scale = input("Введите шкалу измерения:")

temperature(degree, scale)'''

def even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


def digits(num):
    list_num = list(str(num))

    for el in range(len(list_num)):
        list_num[el] = int(list_num[el])

    middleIndex = int((len(list_num) - 1) / 2)
    sum_left_even = sum(list_num[:middleIndex + 1])
    sum_right_even = sum(list_num[middleIndex + 1:])
    sum_left_not_e = sum(list_num[:middleIndex])
    sum_right_not_e = sum(list_num[middleIndex + 1:])
    if even_number(num):
        if sum_left_even == sum_right_even:
            print('11')
        else:
            print('00')
    else:
        if sum_left_not_e == sum_right_not_e:
            print('11')
        else:
            print('00')


number = int(input("Введите число: "))
digits(number)