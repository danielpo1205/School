# A function that takes a positive integer and returns the sum of the cube of all the smaller positive integers

def cube(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n * n
        n -= 1
        return total

print("Sum of cubes: ", cube(4))
print("Bye bye")