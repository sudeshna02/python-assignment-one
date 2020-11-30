# Write a Python program to sum all the items in a dictionary

dict = {'nami_students': 50, 'gyanniketan_students' : 100, 'gyanodaya_students' : 250 }
final_sum = 0

for i in dict.values():
    final_sum = final_sum + i
print(final_sum)

#print(sum(dict.values())