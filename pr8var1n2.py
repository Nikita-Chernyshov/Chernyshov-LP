n=int(input('Введите кол-во строк'))
m=int(input('Введите кол-во столбцов'))
B=[]
for i in range(n):
    b=[]
    for j in range(m):
        print('Введите[',i,',',j,']элемент')
        b.append(int(input()))
        B.append(b)
print('Исходный массив ')
for i in range(n):
    for k in range(m):
        print(B[i][k], end=' ')
        print()
for i in range(n):
    for j in range(m):
        min_b = min(B[i])
        a = B[i].index(min(B[i]))
        tmp1 = B[i][a]
        B[i][0]=B[i][a]
        B[i][a]=tmp1
for i in range(n):
    for j in range(m):
        max_b=max(B[i])
        b=B[i].index(max(B[i]))