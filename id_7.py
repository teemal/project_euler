#Taylor Mallory
#project euler
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

import math

def is_it_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return False
        elif n%i != 0:
            return True

for i in range(1,40):
    print(is_it_prime(i))

iterator = 10

#def get_prime(n):
#    for i in range(1,1000000):
#        if is_it_prime(i) == True:
