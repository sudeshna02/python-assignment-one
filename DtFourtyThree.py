# Write a Python program to remove an item from a tuple.

# creating a tuple
tupl = ('robert', 'patison', 'laxmi', 'prasad', 'devekota')

# checking
print(tupl)

# as tuple are immutable it cannot be converted direclty so converting tuple to list
converted_tupl = list(tupl)

# now using remove function to remove an item
converted_tupl.remove("laxmi")

# now converting the list to tuple
tupl = tuple(converted_tupl)
print(tupl)