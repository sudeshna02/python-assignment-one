#-------------  Question 1   ----------------------------------------#
#python program to count the number of character frequency in a string
# ------------  Solution     ----------------------------------------#
#  using input, in operator, dictionary, for-loop and if else
# taking input string from the user and storing the value in user_input
user_input = input ("Enter a string:")

# task is to count character frequency so creating a empty string
# and keeping the characters from input into dictionary in each
# iteration using for-loop

d1 = dict()
for s in user_input:
    #if character already exists increasing value by 1
    if s in d1:
        d1[s] = d1[s] + 1
    #else assigning new value 1
    else:
        d1[s] = 1
#printing to get the result
print(d1)
