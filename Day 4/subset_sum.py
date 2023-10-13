'''
sum of subsets== target
'''
def check(num,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(num):
            return False
        if backtrack(start+1,sum+num[start]):
            subset.append(num[start])
            return True
        return backtrack(start+1,sum)    
    subset=[]
    if backtrack(0,0):
        return True,subset
    else:
        return False,subset
arr=[1,2,3,6]
n=int(input())
print(check(arr,n))

