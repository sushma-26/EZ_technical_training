def three_pointer_search(arr, target):
    left = 0
    middle = len(arr) // 2
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] == target:
            return left
        if arr[middle] == target:
            return middle
        if arr[right] == target:
            return right
        left += 1
        middle += 1
        right -= 1
    
    return -1  
arr = [9, 7, 5, 3, 1, 2, 4, 6, 8]
target = 6
result = three_pointer_search(arr, target)
print("Element found at index:", result)
