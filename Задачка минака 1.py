
def min_digit(num):
    n = list(str(num))
    c = min(n)
    return c


def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


def first_3_digits(num):
    n = list(str(num))
    n = n[:3]
    return n


def find_range_mean(num):
    n = sum(num) / len(num)
    return n


a = []

for element in range(2020, 67038):
    if sum_of_digits(element) < 10 and min_digit(element) not in first_3_digits(element):
        a.append(element)

print(len(a))
mean_num = find_range_mean(a)
nearest_num = 0

for element in a:
    if abs(mean_num - element) < abs(mean_num - nearest_num):
        nearest_num = element
print(mean_num, nearest_num)