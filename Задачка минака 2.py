def low_numbers(num):
    n = ''.join(sorted(str(num), reverse=True))
    return int(n)


def divisor(num):
    a = []
    for i in range(num, 0, -1):
        if num % i == 0:
            a.append(i)
    if len(a) % 3 == 0:
        return True
    else:
        return False


def first_digit_7(num):
    n = int(str(abs(num))[0])
    if n == 7:
        return num


a_1 = []


for element in range(1082, 24600):  # записывает числа делители котороых кратны 3
    if divisor(low_numbers(element)):
        a_1.append(element)


a_2 = []


for i in range(len(a_1)):
    if a_1[i] == first_digit_7(a_1[i]):
        a_2.append(a_1[i])

print(len(a_1), max(a_2))