#Write a Python program to slice a tuple.

# creating a tuple
# 1   2   3   4   5   6
# 23  24  25  26  27  28
tupl = (23,24,25,26,27,28)
# checking the tuple
print(tupl)

# selecting a element from a tuple
output = tupl[0]
print(output)

# slicing
output = tupl[2:5] #expected: 25. 26. 27
print(output)

#slicing two
output = tupl[4:6] #expected: 27 28
print(output)