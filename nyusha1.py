a=int(input("Введите начало интервала:"))
b=int(input("Введите конец интервала:"))
c=int(input("Введите число:"))
if c in range(a,b):
    print('число попадает в интервал')
else:
    print('число не попадает в интервал')