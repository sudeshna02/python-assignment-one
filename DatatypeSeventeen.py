# Write a Python program to multiplies all the items in a list.
# creating list
givenList = [5, 10, 2]
final_output = 1
# going through list
for i in range(0, len(givenList)):
    # multiplying
    final_output *= givenList[i]
# printing result
print("Multiplication of elements present in the list: ", final_output)