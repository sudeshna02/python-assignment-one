#-------------  Question 8 ------------------------------------------------#
# python program to remove the nth index character from a given string.
# Condition: nonempty
# ------------  Solution   ---------------------------------------------------#
# using function slice, type casting?

def remove_index(string, number):
            first_part = string[:number]
            remaining_part = string[number + 1:]
            return first_part + remaining_part

final_output = remove_index('sudeshna', 2)
print(final_output)

