# def second_largest_element(arr):
#     arr=list(set(arr))
#     arr.sort()
#     if len(arr)>1:
#         return arr[-2]
#     return None
# arr = [3, 5, 7, 2, 8, -1]
# print("The second largest element in the array is:", second_largest_element(arr))

#another way 
def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return "Second largest does not exist"

    return second


arr = [12, 35, 1, 10, 34, 35]

result = second_largest(arr)
print("Second largest element:", result)