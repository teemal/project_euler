#Taylor Mallory
#project euler
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
primes_to_twenty = [2,3,5,7,11,13,17,19]
multi = 1
for p in primes_to_twenty:
    n = 2
    multi *= p
    while (p**n < 21):
        multi *= p
        n += 1

print multi
