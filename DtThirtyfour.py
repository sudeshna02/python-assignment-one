# Write a Python script to merge two Python dictionaries.

#creating dictionary
dict_one = {'id' : 1, 'name' : 'sudeshna'}
dict_two = {'surname' : 'pandey', 'salary' : 1000}
final_output = {}
# final_output.update(dict_one)
# final_output.update(dict_two)

final_output = {**dict_one, **dict_two}
print(final_output)

