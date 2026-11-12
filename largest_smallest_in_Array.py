def largest_element(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

def smallest_element(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr = [3, 5, 7, 2, 8, -1]
print("The largest element in the array is:", largest_element(arr))
print("The smallest element in the array is:", smallest_element(arr))