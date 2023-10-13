def two_pointer_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        left += 1
        right -= 1
    
    return -1  

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = two_pointer_search(arr, target)
print("Element found at index:", result)
