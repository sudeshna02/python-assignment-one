# Write a Python program to multiply all the items in a dictionary

dict = {'nami_students': 3, 'gyanniketan_students' : 2, 'gyanodaya_students' : 2 }
final_multi = 1

for i in dict.values():
    final_multi = final_multi * i
print(final_multi)

#print(sum(dict.values())