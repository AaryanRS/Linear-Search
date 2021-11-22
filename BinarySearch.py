print("Welcome to Binary Search")

arr = sorted([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def BinarySearch(arr,start,end,x):
    if end >= start:
        mid = start +(end - start) // 2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr , start, mid - 1, x)
        elif arr[mid] < x:
            return BinarySearch(arr , mid + 1, end , x)
    else :
        return "Not Found"

x = int(input("Please Enter the number: "))
result = BinarySearch(arr, 0 , len(arr) - 1, x)
print(f"the{x} is at {result}")
