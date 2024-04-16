# Generator comprehension

# This avoid storing an unnecessary amount of values until you need to use it
# sum ask for each values sequentialy and add it to a sum that its storing internally
sum_of_squares = sum(x**2 for x in range(1000000))

"""
Generator:
 A Generator only return values when they need to be use

 # Quick Summary
 # Returns values when needed
 # Gives next value
 """