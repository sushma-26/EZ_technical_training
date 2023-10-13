s1=input()
s2=input()
i=j=0
if len(s1)>len(s2):
    n=len(s1)
    n2=len(s2)
else:
    n2=len(s1)
    n=len(s2)
s=""
k=0
while i<n:
    if s1[i]==s2[j]:
        while j<n2:
            if s1[i]!=s2:
                k=1
                break
            s+=s1[i]
            i+=1
            j+=1
        
    else:
        i+=1
    if k==1:
        s=""
    
print(s)