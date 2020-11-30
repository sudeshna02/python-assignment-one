# Write a Python function to check whether a number is in a given range.

# defining a function to check a number
def within_range(numb):
    if numb in range(1,10):
        print(f"The number is within range from 1 to 10.")
    else:
        print("The number is not in range!")
# printing to check result
print(within_range(1))