# A function that takes a positive integer and returns the sum of the cube of all the smaller positive integers

def cube(n):
    n = n-1
    total = 0
    while n > 0:
        total = total + (n * n * n)
        n = n-1
    return total

print("Sum of cubes: ", cube(5))
print("Bye bye")


# # Another option to solve this:
# def positive(num):
#     sum=0
#     for i in range(1,num):
#         sum=sum+(i**3)
#     print("The summary is: ", str(sum))
#     return sum
#
# new_sum=positive(int(input("Enter a positive number: ")))