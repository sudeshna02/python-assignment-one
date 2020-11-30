#-------------  Question 7 ------------------------------------------------#
# python program to take list of words and returns the length of
# longest one.
# ------------  Solution   ---------------------------------------------------#
# using split, length, for loop and if

# taking the input string from the user and storing the value in user_input
user_input = input ("Enter the line of strings:")
splitted_input = user_input.split()

longest_one = len(splitted_input[0])

for i in splitted_input:
    if len(i) > longest_one:
        longest_one = len(i)
print('The length of longest one from the input is:', longest_one)