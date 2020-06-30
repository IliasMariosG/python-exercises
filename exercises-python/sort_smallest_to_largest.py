# sort an array from smallest to largest.

def find_smallest_index(numbers):
    """find the smallest index

    >>> find_smallest_index([141, 156, 35, 94,  88, 61, 111])
    2
    """
    smallest_value = numbers[0]
    smallest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < smallest_value:
            smallest_value = numbers[i]
            smallest_index = i
    return smallest_index

def selection_sort(numbers):
    """show the correct sorted array

    >>> selection_sort([141, 156, 35, 94,  88, 61, 111])
    [35, 61, 88, 94, 111, 141]
    """
    new_arr =[ ]
    for i in range(1, len(numbers)):
        find_smallest_index(numbers)
        #print(type(find_smallest(numbers)))
        #print(numbers)
        #print(find_smallest_index(numbers))
        new_arr.append(numbers.pop(find_smallest_index(numbers)))
        #(new_arr)
    return new_arr

# (find_smallest_index([141, 156, 35, 94,  88, 61, 111]))
# print(selection_sort([141, 156, 35, 94,  88, 61, 111]))