def zam(x):
    appa = 0
    for i in range(5):
        appa += x[i]
        print('Сумма', appa)
        appa = appa/5
        print('Средн. арифметическое', appa)
        return appa
def spam(y):
    appa = 0 
    for i in range (5):
        appa += y[i]
        print('Сумма', appa)
        appa = appa/5
        print('Средн.арифметическое',appa)
        return appa
def cam(z):
    appa = 0 
    for i in range (5):
        appa += z[i]
        print('Сумма', appa)
        appa = appa/5
        print('Средн.арифметическое',appa)
        return appa
A=[]
for i in range(5):
    A.append(int(input('Введите элемент массива А')))
B=[]
for i in range(5):
    B.append(int(input('Введите элемент массива B')))
C=[]
for i in range(5):
    C.append(int(input('Введите элемент массива C')))
print(zam(A))
print(spam(B))
print(cam(C))