#palindrome in a string return True/False
def valid_pal(s):
    n=len(s)
    def is_pal(l,r):
        while l>=0 and r<n and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    res=[]
    for i in range(len(s)):
        pal1=is_pal(i,i)
        if len(pal1)>1:
            res.append(pal1)
        pal2=is_pal(i,i+1)
        if len(pal2)>1:
            res.append(pal2)
    return res
        
l=input()
print(valid_pal(l))


