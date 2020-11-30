#-------------  Question 6 ------------------------------------------------#
# python program to find the first appearance of the substring
# 'not' and 'poor' from a given string.
# Condition : if 'not' follows the 'poor', replace the whole with 'good' and
# return string
# ------------  Solution   ---------------------------------------------------#
# using string slicing, operator and if else
# taking the input string from the user and storing the value in user_input
user_input = input ("Enter the line of strings to find substring:")
get_not = user_input.find("not")
get_poor = user_input.find("poor")

if(get_poor > get_not and get_not > 0 and get_poor > 0):
    final_output = user_input.replace(user_input[get_not:get_poor+4], 'good')
    print(final_output)
else:
    print(user_input)

