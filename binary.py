def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1

    print(low)
    print(high)

    while low <= high:
        mid = (low + high)//2
        guess = input_list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        print(low)
        print(high)
    return None

input_list = [1, 5, 10, 11, 30, 31, 32, 34, 35, 50, 101, 299]
output_index = binary_search(input_list, 13)
if output_index == None:
    print("Item not in list.")
else:
    print(input_list[output_index])
    assert output_index == 4, "Output index should equal 4"
    assert input_list[output_index] == 30, "Indexed number should be equal to 30"
