#-------------  Question 10  ------------------------------------------------#
# python program to get a string after removing char from odd index of
# a given string
# Condition :
# ------------  Solution   ---------------------------------------------------#
# using string range, len, in operator
# taking the input string from the user and storing the value in user_input
# 0 1 2 3 4 5 6 7
# s u d e s h n a
# 1 3 5 7
# u e h a
user_input = input ("Enter the string:")
final_output = ""

for i in range(len(user_input)):
    if(i%2==0):
        final_output += user_input[i]
print(final_output)


