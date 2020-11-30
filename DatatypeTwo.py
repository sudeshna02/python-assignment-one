#-------------  Question 2  ------------------------------------------------#
# python program to get a string made of the first and last 2 character from
# a given string
# Condition : if string length is less than two output should be "empty string"
# ------------  Solution   ---------------------------------------------------#
#  using string slicing, len() and if else
# taking input string from the user and storing the value in user_input
user_input = input ("Enter a string:")
final_output = ""

# fulfilling condition 1
if len(user_input) < 2:
    final_output = "Empty String!"
# taking first and last two characters using slicing, and combining two in output
# using + operator
else:
    first_two = user_input[0:2]
    last_two = user_input[-2:]
    final_output = first_two + last_two
#printing to get the result
print(final_output)
