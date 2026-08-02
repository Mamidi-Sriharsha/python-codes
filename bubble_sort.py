n=int(input("enter the number of elements: "))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("sorted array is:",arr)