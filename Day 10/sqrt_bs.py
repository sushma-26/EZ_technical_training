def mySqrt(x):
        if x<2:
            return x
        def sqrt(x,s,e,floor):
            if s<=e:
                n=(s+e)//2
                sq=n*n
                if sq==x:
                    return n
                elif sq<x:
                    return sqrt(x,n+1,e,n)
                else:
                    return sqrt(x,s,n-1,floor)
            return floor
        s=sqrt(x,0,x//2,-1)
        return s
n=int(input())
print(mySqrt(n))