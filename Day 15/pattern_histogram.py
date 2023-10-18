'''
[2,3,0,5]
**
***

*****
for i in range(n):
    print("*"*l[i])
[2,3,0,5]
    *
    *
 *  *
**  *
**  *
'''
l=list(map(int,input().split()))
n=max(l)
m=len(l)
for i in range(n,0,-1):
    print(f"{i:2d} |",end="")
    for j in l:
        if j>=i:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()

    


