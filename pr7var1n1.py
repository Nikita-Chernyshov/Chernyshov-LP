def fig(a,b,h):
    s1= 1/2 * a * h
    print('Площадь треугольника', s1)
    s2= a*a
    print('Площадь квадрата', s2)
    s3= (a+b)/2 * h 
    print('площадь трапеции', s3)
    return s1, s2, s3
x=int(input('Введите x'))
y=int(input('Введите y'))
z=int(input('Введите z'))
print(fig(x,y,z))
