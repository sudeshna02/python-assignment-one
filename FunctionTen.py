# Write a Python program to print the even numbers from a given list.
# --- solution -------

# creating a list
lst = [1,2,3,4,5,6,7,8,9,10]
output = []

# defining a function to print even number
def filter_even(list):
    for i in list:
        if i%2 == 0:
            output.append(i)
    return output
# printing to get the result
print(filter_even(lst))