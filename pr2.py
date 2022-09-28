import math
x=2.444
y=0.00869
z=-1300
s=((((1+math.fabs(y-x))*x**(y+1)+math.e**(y-1))/(1+x*math.fabs(y-math.atan(z)))+(((math.fabs(y-x)**2))/2)-(((y-x)**3)/3)))
print(s)