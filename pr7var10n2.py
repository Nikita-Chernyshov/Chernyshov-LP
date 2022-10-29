def raz(a):
    b = list(reversed(a.split(" ")))
    return b
c = input('Введите строку')
print(raz(c))