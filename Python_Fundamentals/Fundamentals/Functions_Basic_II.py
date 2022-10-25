# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(element):
    newList = []
    while(element >= 0):
        newList.append(element)
        element -= 1
    return newList

print(countdown(5))


# Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(arr):
    print(arr[0])
    return(arr[1])

print(print_and_return([1,2]))


# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(arr):
    return(arr[0] + len(arr))

print(first_plus_length([1,2,3,4,5]))


# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(arr):
    newList = []
    if(len(arr) < 2):
        return False
    for i in arr:
        if i > arr[1]:
            newList.append(i)
    print(len(newList))
    return newList

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(a,b):
    newList = []
    for i in range(0,a):
        newList.append(b)
    return newList

print(length_and_value(4,7))
print(length_and_value(6,2))