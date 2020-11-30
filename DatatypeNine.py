#-------------  Question 9  ------------------------------------------------#
# python program to get a string by exchanging first and last char from
# a given string
# Condition :
# ------------  Solution   ---------------------------------------------------#
# using string slicing, operator
# taking the input string from the user and storing the value in user_input
user_input = input ("Enter the string:")

# slicing the last three characters from the input string
last_one = user_input[-1:]
other_one = user_input[1:-1]
first_one = user_input[0]

final_output = last_one + other_one + first_one
print(final_output)