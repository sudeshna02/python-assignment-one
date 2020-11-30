# Write a Python function to multiply all the numbers in a list.
# -------- Solution ----------------------------------

# creating a list
created_list = [2,3,4,5,6]

# defining a function to multiply all the numbers
def multiplyList(list):
    mult = 1
    for i in list:
        mult *= i
    return mult

# printing the output
print(multiplyList(created_list))