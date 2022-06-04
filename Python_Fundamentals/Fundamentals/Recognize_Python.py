num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # Boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # initialize tuples
print(type(fruit)) # type check, log statement
print(pizza_toppings[1]) # log statement, access value list
pizza_toppings.append('Mushrooms') # add value list
print(person['name']) # log statement, access value dictionary
person['name'] = 'George' # change value dictionary
person['eye_color'] = 'blue' # change value dictionary
print(fruit[2]) # log statement, access value list

if num1 > 45: # if conditional
    print("It's greater") # log statement
else: # else conditional
    print("It's lower") # log statement

if len(string) < 5: # if conditional
    print("It's a short word!") # log statement
elif len(string) > 15: # else if conditional
    print("It's a long word!") # log statement
else: # else conditional
    print("Just right!") # log statement

for x in range(5): # start for loop
    print(x) # log statement, stop for loop
for x in range(2,5): # start for loop
    print(x) # log statement, stop for loop
for x in range(2,10,3): # start for loop, increment
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # start while loop
    print(x) # log statement
    x += 1 # sequence while loop, break while loop when x is 5

pizza_toppings.pop() # delete value list
pizza_toppings.pop(1) # delete value list

print(person) # log statement, initialize dictionary
person.pop('eye_color') # delete value dictionary
print(person) # log statement, initialize dictionary

for topping in pizza_toppings: # start for loop
    if topping == 'Pepperoni': # if conditional, variable check
        continue # continue for loop
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if conditional, variable check
        break # break for loop

def print_hello_ten_times(): # function parameter
    for num in range(10): # start for loop
        print('Hello') # log statement

print_hello_ten_times() # calling function without argument

def print_hello_x_times(x): # function parameter
    for num in range(x): # start for loop
        print('Hello') # log statement

print_hello_x_times(4) # calling function with argument

def print_hello_x_or_ten_times(x = 10): # function parameter
    for num in range(x): # start for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # calling function without argument
print_hello_x_or_ten_times(4) # calling function with argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)