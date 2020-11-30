#  Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# ----- solution ----------------------------
input_string = "I love Python"

# defining the function to calculate upper and lower case letters

def letter_calculate(string):
    lower_count = 0
    upper_count = 0
    # going through string
    for i in string:
        # checking count of lower and upper character
        if i.islower():
            lower_count = lower_count + 1
        elif i.isupper():
            upper_count = upper_count + 1

    print(f"Lower count: {lower_count}")
    print(f"Upper count: {upper_count}")

letter_calculate(input_string)