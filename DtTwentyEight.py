# Write a Python script to add a key to a dictionary.

dict = {'id' : 1, 'name' : 2 }

def add_key(key, value):
    dict[key] = value
    return dict

print(add_key('surname', 3))