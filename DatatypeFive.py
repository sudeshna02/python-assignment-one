#-------------  Question 5  ------------------------------------------------#
# python program to get a string by adding ing into the given string
# Condition : input string length should be greater than 3 and if ing already
# exists add ly instead
# ------------  Solution   ---------------------------------------------------#
# using string slicing, operator and if else
# taking the input string from the user and storing the value in user_input
user_input = input ("Enter the string:")

# slicing the last three characters from the input string
last_one = user_input[-3:]

# if length is greater than 3 adding ing and ly else leaving it unchanged
if len(user_input) >=3:
    if last_one == "ing":
        final_output = user_input + "ly"
    else:
        final_output = user_input + "ing"
    print(final_output)
else:
    print(user_input)