# Блок Б Задание 4
n=int(input('Введите число: '))
def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            rrr='NO'
            break
        else:
            rrr='YES'
    return(rrr)
print(isPrime(n))