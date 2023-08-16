#SELECTION SORT''' START '''''' START '''''' START '''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input 
input_str = input("Enter the elements separated by spaces: ")
arr = [int(x) for x in input_str.split()]

selection_sort(arr)
print("Sorted array:", arr)



#INSERTION SORT  ''' START '''''' START '''''' START '''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input 
input_str = input("Enter the array elements separated by spaces: ")
arr = [int(x) for x in input_str.split()]

insertion_sort(arr)
print("Sorted array:", arr)

# Quick SORT ''' START '''''' START '''''' START '''''' START '''


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Input 
input_str = input("Enter the array elements separated by spaces: ")
arr = [int(x) for x in input_str.split()]

sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
