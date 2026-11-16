def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
arr=[11,22,33,44,55]
print("Original array:", arr)
print("Reversed array:", reverse_array(arr))