'''
Towers of hanoi
'''
def toh(n,s,a,d):
    if n>0:
        toh(n-1,s,d,a)
        print("moves",n,"from",s,"to",d)
        toh(n-1,a,s,d)
n=int(input())
toh(n,"source","aux","dest")