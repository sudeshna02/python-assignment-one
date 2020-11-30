# Write a Python program to insert a given string at the beginning of all items in
# a list.

created_list = [1,4,5,6,8]
output = []

for i in created_list:
    output.append(f"inst{i}")

print(output)