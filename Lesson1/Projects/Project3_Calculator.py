# Reading an integer (n) and then computing it - n+nn+nnn

from time import sleep

N = int(input("Please enter a number: \n"))
N1 = int("%s" % N)
N2 = int("%s%s" % (N,N))
N3 = int("%s%s%s" % (N,N,N))
sleep(2)
print("Working....")
sleep(2)
print("The result is: ", int(N1+N2+N3))

### another way:
# print(n+ (n*10+n) + (n*100+n*10+n))