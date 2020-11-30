#-------------  Question 3  ------------------------------------------------#
# python program to get a string where the occurrences of first char have
# been changed to $ from a given string
# Condition : except the first character
# ------------  Solution   ---------------------------------------------------#
#  using string slicing and replace
# taking input string from the user and storing the value in user_input
user_input = input ("Enter a string:")

# taking the first character from input
first_one = user_input[0]
# taking the remaining character from input
other_one = user_input[1:]
# replacing using replace function
changed_input = other_one.replace(first_one, "$")
# combining both
final_output = first_one + changed_input

#printing to get the result
print(final_output)