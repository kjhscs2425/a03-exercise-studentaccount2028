
# #Write a function `print_multiples` with one parameters `n`.

def print_multiples (n):
    multiples = []
    # When called, your function should print out ALL of the multiples of `n` between 0 and 100 (including both 0 and 100), and NO OTHER numbers.
    for i in range(1,100):
        if n%i == 0:
            multiples.append(i)
    print(multiples)
            


# Call your function for `n = 2`, `n = 3`, `n = 5`, and `n = 12`.
print_multiples(2)
print_multiples(3)
print_multiples(5)
print_multiples(12)
