#Taylor Mallory
#project euler num 2

store_fib = []

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# Display the first 15 Fibonacci numbers.
for c in range(0, 35):
    fibber = fibonacci(c)
    if fibber % 2 == 0 and fibber <= 4000000:
        store_fib.append(fibber)
    #print(fibonacci(c))
print(store_fib)
print(sum(store_fib))
