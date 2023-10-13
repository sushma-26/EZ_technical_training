def gen(n):
    i=n//2
    j=n-1
    k=1
    m=[[0]*n for i in range(n)]
    def fill(i,j,k):
        if k>n*n:
            return m
        if i<0 and j==n:
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if m[i][j]:
            i=i+1
            j=j-2
            return fill(i,j,k)
        m[i][j]=k
        return fill(i-1,j+1,k+1)
    return fill(i,j,k)
n=int(input())
m=gen(n)
for i in m:
    print(*i)
