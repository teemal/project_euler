#Taylor Mallory
#projt_euler

divisible = []
for i in range (0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            divisible.append(i)

print(sum(divisible))
