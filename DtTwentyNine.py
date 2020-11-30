# Write a Python script to concatenate 4ef dictionaries to create a new
# one.

dict_one = {0: 1, 1:20}
dict_two = {2:30, 4:50}
dict_three = {5:60, 6:70}
final_dict = {}

for i in (dict_one, dict_two, dict_three):
    final_dict.update(i)

print(final_dict)