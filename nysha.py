a = int(input('Введите целое число'))
x = int(input('Введите целое число'))
if (x == 3 and a > 3):
	y=x+a
elif (a == 4 or x < 2):
	y=x*a
else:
    y=x**a
print(y)
