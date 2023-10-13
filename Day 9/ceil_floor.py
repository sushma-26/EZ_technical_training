def bs_floor(l,target):
    start=0
    end=len(l)-1
    floor=-1
    while(start<=end):
        mid=(start+end)//2
        if l[mid]==target:
            floor=l[mid]
            break
        elif l[mid]<target:
            floor=l[mid]
            start=mid+1
        else:
            ceil=l[mid]
            end=mid-1
    print(floor,"floor")
    print(ceil,"ceil")
l = [1,2,4, 9, 99]
bs_floor(l,10)