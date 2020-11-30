#  Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def count_filter(string):
    count = 0
    for i in string:
        if i[0] == i[-1]:
            count += 1
    return count

print(count_filter(["abc", "ab", "asudshna", 'ct']))