def quicksort(arr):
    # base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # choose a pivot (middle is a safe/simple choice)
    pivot = arr[len(arr) // 2]

    # partition into three lists
    left = [x for x in arr if x < pivot]     # smaller than pivot
    middle = [x for x in arr if x == pivot]  # equal to pivot
    right = [x for x in arr if x > pivot]    # greater than pivot

    # recursively sort left and right, then combine
    return quicksort(left) + middle + quicksort(right)


# test it
nums = [10, 1, 8, 9, 6, 5]
print(quicksort(nums))