from random import randint
print ('На отрезке [100,N] (210,n,231) найти кол-во чисел, составленных из цифр a,b,c')
def find(N):
    schet = 0
    b = []
    arr = [i for i in range (0, 10)]
    for i in arr:
        for k in arr:
            for s in arr:
                if s!=k and k!=i and s!=i:
                    z=s*100 + k*10+i
                    if z>=100 and z<N:
                        return schet
N=int(input('Введите 210 < N < 231'))
while N < 210 or N> 231:
    print('Неверное значение')
    N=int(input())
print(find(N)) 
