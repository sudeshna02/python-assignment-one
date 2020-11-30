# Write a Python program to check whether all dictionaries in a list are empty or
# not.

created_list = [{4,8}, {}]
print(all(not i for i in created_list))