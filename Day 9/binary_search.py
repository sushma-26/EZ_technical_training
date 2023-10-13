def binarySearch(l,si,li,k):
    if si>li:
        return li
    mid=(si+li)//2
    if l[mid]==k:
        return mid
    if l[mid]<k:
        return binarySearch(l,mid+1,li,k)
    return binarySearch(l,si,mid-1,k)
l = [1,2,4, 9, 99]
print(binarySearch(l, 0, len(l), 3))