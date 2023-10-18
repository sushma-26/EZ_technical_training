#sieve of erasthones
n=int(input())
l=[True]*(n+1)
l[0]=l[1]=l[2]=True
i=2
while(i*i<=n):
    if l[i]:
        for j in range(i * i, n + 1, i):
            l[j] = False
    i+=1
for i in range(n+1):
    print(l[i],"==>",i)
'''
for i in range(2,n):
        if l[i]==True:
              for j in range(i * i, n + 1, i):
                l[j] = False
'''