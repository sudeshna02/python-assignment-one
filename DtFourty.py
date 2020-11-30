# Write a Python program to add an item in a tuple.

# creating a tuple
tupl = (2, 3, 4, 5, 6, 7)

# tupl are immutable so converting them into list first
converted_tupl = list(tupl)
# adding the items into the list
converted_tupl.append(30)
# now again converting it into tuple
tupl = tuple(converted_tupl)
print(tupl)
