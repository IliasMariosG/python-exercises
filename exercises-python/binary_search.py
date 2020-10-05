def binary_search(numbers, target_value):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        # if (low + high)%2 == 0:
        mid = round((low + high) / 2)
        # else:
            # mid = round((low + high) / 2 + 0.5)
        guess = numbers[mid]
        if guess == target_value:
            return mid, guess
        elif guess < target_value:
            
            low = mid + 1
        else:
            high = mid - 1     
    return None

# print(binary_search([0, 1, 45], 0))
print(binary_search([0, 1, 3, 20, 33, 35], 35))




# # SORTING A LIST (in ascending order)
# l = [1,2,7,3,5]
# l = sorted(l)
# # OR
# l.sort()
# print(l)