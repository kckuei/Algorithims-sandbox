def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

unsorted = [5, 3, 6, 2, 10]
print(unsorted)
sorted = selection_sort(unsorted)
print(sorted)
assert sorted== [2, 3, 5, 6, 10], "output should equal [2, 3, 5, 6, 10]"
