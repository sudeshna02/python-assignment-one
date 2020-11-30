# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

user_input = input ("Enter the words separated with comma:")
splited_output = user_input.split(",")

sort_input = sorted(splited_output)

final_output = ",".join(sort_input)
print(final_output)