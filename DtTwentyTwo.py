# Write a Python program to remove duplicates from a list.

created_list = [1,2,2,2,23,4,5,6,7]
dup_remove_list = list(dict.fromkeys(created_list))

print(dup_remove_list)