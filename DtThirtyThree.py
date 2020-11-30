# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

def square():
    dict = {x : x*x for x in range(1,16)}
    return dict

print(square())