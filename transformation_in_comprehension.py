# List comp with functions
def square(x):
    return x**2

squared_numbers = [square(x) for x in range(10)] #if x % 2 == 0]
print(squared_numbers)
