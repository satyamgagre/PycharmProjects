# SORTING ALGORITHMS

## BUBBLE SORT
# Bubble sort repeatedly compares and swaps adjacent elements until the list is sorted, moving larger elements to the end with each pass.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):  # Optimized inner loop
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
data = [34, 54, 26, 865, 3532, 123, 654]
bubble_sort(data)
print("Bubble Sort: \n",data, "\n")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
##SELECTION SORT
# Selection sort repeatedly finds the smallest element from the unsorted part of the list and swaps it with the first unsorted element.

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
# Example usage
selection_sort(data)
print("Selection Sort: \n",data, "\n")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
##INSERTION SORT
# Insertion sort builds the sorted list one element at a time by inserting each new element into its correct position among the already sorted elements.

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
# Example usage
insertion_sort(data)
print("Insertion Sort: \n",data, "\n")