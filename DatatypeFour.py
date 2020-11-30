#-------------  Question 4  ------------------------------------------------#
# python program to get a string separated by a space and by swapping the
# first two characters of from the given two strings
# Condition :
# ------------  Solution   ---------------------------------------------------#
#  using string slicing and operator
# taking the two input strings from the user and storing the value in user_input
# and user_input_two
user_input = input ("Enter first string:")
user_input_two = input( "Enter second string:")

# slicing the first two character and remaining character from first input
first_one = user_input[0:2]
other_one = user_input[2:]

# slicing the first two character and remaining character from second input
second_one = user_input_two[0:2]
other_two = user_input_two[2:]

# combining to get the result separated by a space
final_output = second_one + other_one + " " + first_one + other_two

# printing to get the result
print(final_output)
