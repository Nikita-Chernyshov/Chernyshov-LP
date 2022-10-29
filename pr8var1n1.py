N = int(input('Введите размер матрицы'))
a = []
for i in range(N):
    b = []
    for j in range[N]:
        print('Введите [ ', i ,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
print('Исход. массив')
for i in range(N):
    for j in range(N):
        print(a[i][j], end=' ')
    print()
k = 0
s = 0
for i in range(N):
    for j in range(N):
        if i < j:
            s = s + a[i][j]
            if a[i][j] > 0:
                k += 1
print('Сумма элементов над главной диагональю', s)
print('Кол-во положит. элементов', k)