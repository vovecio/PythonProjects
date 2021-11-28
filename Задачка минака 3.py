def prime_digit(num):
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


print(len(list_of_number_2))


