#Taylor Mallory
#project euler
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
import math

def sum_of_squares(n):
    start = 0
    for i in range(1,n + 1):
        start += math.pow(i, 2)
    return start


def square_of_sums(n):
    start = 0
    for i in range(1, n + 1):
        start += i
    power = math.pow(start, 2)
    return power

print(square_of_sums(100) - sum_of_squares(100))
