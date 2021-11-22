print("Welcome to Linear Search")

arr = [33,6,8,2,9,45,67,2,3,78,56,87,23,34,16,76,1,1]

def linearSearch(arr, x) :
    for i in range (len(arr)):
        if arr[i] == x :
            return f"Found at {i}"
    return "Not Found"

x = int(input("Please enter a number to search: "))
result = linearSearch(arr , x)
print(result)

