
N=int(input())
a=[]
a2=[]
for i in range(N):
    x=int(input())
    a.append(x)
for i in range(N):
    y=int(input())
    a2.append(y)
a3=[a&a2]
a3.sort()
print(a3)    
