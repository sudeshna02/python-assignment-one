# Write a Python function that takes a number as a parameter and check the
# number is prime or not.

# ---- solution -------

# defining a function to check prime number
def prime_check(numb):

    # checking if its a prime number
    if numb > 1:
        for i in range(2, numb):
            if numb%i == 0:
                return False
                break
        return True
    else:
        return False

# printing to get a result
print("Its a prime number!" if prime_check(17)
      else "Its not a prime number.")