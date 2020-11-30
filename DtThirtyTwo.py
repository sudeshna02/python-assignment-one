# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

def square(numb):
    dict = {x : x*x for x in range(1,numb+1)}
    return dict

print(square(5))