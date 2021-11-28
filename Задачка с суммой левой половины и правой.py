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