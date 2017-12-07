#Taylor Mallory
#project euler
#Find the largest palindrome made from the product of two 3-digit numbers.
store = []
def is_palindrome(n):
    num = str(n)
    rev = num[::-1]
    return rev == num


for i in range(999,99, -1):
    for j in range(999,99, -1):
        test = i * j
        if is_palindrome(test) == True:
            print(test)
            break
        #if is_palindrome(i * j) == True:
        #        store.append(i)
        #        store.append(j)
        #        print(store)
        #        break
