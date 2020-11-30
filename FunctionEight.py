#  Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

# ---- solution ----------------
# defining list
lst = [1,2,4,3,5,6,2,2]
output = []
# defining function to return unique elements of the first list

def unique_ele(a):
    for i in a:
        if i not in output:
            output.append(i)
    return output

print(f"Unique Elements {unique_ele(lst)}")