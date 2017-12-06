#Taylor Mallory
#project euler
import math

def is_it_prime(n):
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
            return True
#print(is_it_prime(13))

def get_largest_prime_fac(m):
    holder = m / 2
    if is_it_prime(holder) != True:
        
