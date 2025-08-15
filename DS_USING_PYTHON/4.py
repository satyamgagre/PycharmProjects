# SEARCHING ALGORITHMS

# Linear Search Algorithm
# Linear search sequentially checks each element in a list until the target is found or the end of the list is reached.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found, return index
    return -1  # Not found

# Example usage
numbers = [1, 4, 3, 12, 5, 6, 7, 8, 9]
target = 1
result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Binary Search Algorithm
# Binary search repeatedly divides the sorted list in half, comparing the middle element to the target,
# and continues in the half where the target may lie until it’s found or the range is empty.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Sorted list (required for binary search)
numbers = sorted([1, 4, 3, 12, 5, 6, 7, 8, 9])
target = 1
result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
