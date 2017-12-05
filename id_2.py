#Taylor Mallory
#project euler num 2

store_fib = []

def fib(end_num):
    x = 1
    y = 2
    store_fib.append(x)
    store_fib.append(y)

    if x >= end_num:
        x = False
    while (x != False):
        adder = store_fib[len(store_fib)] + store_fib[len(store_fib - 1)]
        store_fib.append(adder)
        fib(end_num)

fib(100)
