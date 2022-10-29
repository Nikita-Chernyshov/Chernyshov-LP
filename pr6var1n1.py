mas=[]
n = 5
for i in range(n):
    mas.append(input('Введите число: '))
 
print('максимальный элемент: ' + str(max(mas)))
print('обратный порядок: ' + str(list(reversed(mas))))
