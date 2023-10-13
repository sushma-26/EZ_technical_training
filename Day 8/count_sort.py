l=list(map(int,input().split()))
c=[0 for i in range(len(l)+1)]
res=[0]*len(l)
for i in l:
    c[i]+=1
for i in range(1,len(c)):
    c[i]+=c[i-1]
print(c)
for i in range(len(l)):
    res[c[l[i]]-1]=l[i]
    c[l[i]]-=1
print(res)
