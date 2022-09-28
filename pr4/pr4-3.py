a=int(input("Введите первое число"))
b=int(input("Введите второе число"))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')