l=list(map(int,input().split()))
t=int(input())
n=len(l)
i=0
j=0
csum=l[0]
while i<n:
    if csum == t:
        print(i,j,csum)
        break
    elif csum > t:
        csum-=l[i]
        i+=1
    else:
        j+=1
        csum+=l[j]
