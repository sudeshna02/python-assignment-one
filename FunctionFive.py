# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

# defining the function to calculate factorial
def factorial_calculate(numb):
    fact = 1
    while numb > 0:
        fact = fact * numb
        numb = numb - 1
    return fact
# printing to get a result
print(factorial_calculate(3))