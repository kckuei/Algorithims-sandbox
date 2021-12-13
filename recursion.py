# Think about the base case, and the recursive case 

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

def count_items(arr):
    if arr == []:
        return 0
    else: 
        return 1 + count_items(arr[1:])

def max_number(arr, current_max=-float("inf")):
    if arr == []:
        return current_max
    else:
        if current_max < arr[0]:
            return max_number(arr[1:], arr[0]) 
        else:
            return current_max

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

def quicksort(arr):
    # The speed of quicksort depends on the pivot chosen

    # base case for arrays with 0 or 1 element; already sorted
    if len(arr) < 2:
        return arr 
    else:
        pivot = arr[0]

        # sub-array of all elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]

        # sub-array of all elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)




print(factorial(5))

print(sum([2,4,6]))

print(count_items([1,2,3,"four",5]))

print(max_number([2,3,4,23,10]))

arr = [2, 3, 4, 10, 40, 63, 1000]
item = 40
print(binary_search(arr, 0, len(arr)-1, item))


print(quicksort([89, 100, 23, 22, -5, 63, 23, 11]))