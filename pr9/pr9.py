x=[]
n=0
maxx=minn=maxi=mini=0
with open('Chernyshov_Nikita_UB22_vvod.txt','r') as file:
    for line in file:
        x.append( list(map(int, line.split() )))
        n+=1
for i in range(n):
      for j in range(n): 
          if i==0 and j==1:maxx=minn=x[0][0]+x[0][1]
          if j>0:
              if x[i][j-1]+x[i][j]>maxx:
                  maxx=x[i][j-1]+x[i][j]
                  maxi=i
              if x[i][j-1]+x[i][j]<minn:
                  minn=x[i][j-1]+x[i][j]
                  mini=i
file.close()
with open('Chernyshov.Nikita_UB22_vivod.txt','w') as file1:
        print(file1.write("max summ = "))
        print(file1.write(str(maxx)))
        print(file1.write('\n'))
        for j in range(n): 
            print(file1.write(str(x[maxi][j])))
            print(file1.write(" "))
        print(file1.write('\n'))
        print(file1.write("min summ = "))
        print(file1.write(str(minn)))
        print(file1.write('\n'))
        for j in range(n): 
            print(file1.write(str(x[mini][j])))
            print(file1.write(" "))
        print(file1.write("\n"))
        print(file1.write("new matrix\n"))
        for i in range (n):
               for j in range(n):
                    if x[i][j]<0 :x[i][j]=0
                    else: x[i][j]=1
        for i in range (n):
            for j in range(n):
                if i>=j: 
                    print (file1.write(str(x[i][j])))
                    print(file1.write(" "))
            print(file1.write("\n"))
file1.close()