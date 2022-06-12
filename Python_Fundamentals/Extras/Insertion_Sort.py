arr = [8,5,2,6,9,3,1,4,0,7]

def sort():
    for i in range(len(arr)):
        key = arr[i]
        for j in range(i+1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                print(arr)

print(sort())