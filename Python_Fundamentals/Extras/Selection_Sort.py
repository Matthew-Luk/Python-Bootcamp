arr = [8,5,2,6,9,3,1,4,0,7]

def sort():
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1,(len(arr))):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

print(sort())