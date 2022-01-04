
a = []
while True:
    n = input()
    if n == '.':
        break
    else:
        a.append(float(n))


print(min(a))