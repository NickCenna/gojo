
#Linear search 

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

input_str = input("Enter the array elements separated by spaces: ")
arr = [int(x) for x in input_str.split()]
target = int(input("Enter the element to search: "))
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")


    
#Binary search


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

input_str = input("Enter the sorted array elements separated by spaces: ")
arr = [int(x) for x in input_str.split()]
target = int(input("Enter the element to search: "))
index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
    
