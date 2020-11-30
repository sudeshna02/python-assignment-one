# Write a Python program to sum all the items in a list.
# creating list
givenList = [5, 10, 15, 20, 25, 30]
final_output = 0
# going through list
for i in range(0,len(givenList)):
    # adding elements
    final_output = final_output + givenList[i]
# printing the sum
print("Sum of elements present in the list: ", final_output)
