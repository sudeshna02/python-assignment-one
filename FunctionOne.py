# 1. Write a Python function to find the Max of three numbers.
## ------ solution --------

# defining a function named maximumNumber to take in three numbers
def maximumNumber(first, second, third):
    #comparing to get the maximum number using if and else if
    if first>second and first>third:
        maximum = first
    elif second>first and second>third:
        maximum = second
    else:
        maximum = third
    return maximum
# printing to get result
print(maximumNumber(12, 121,32))