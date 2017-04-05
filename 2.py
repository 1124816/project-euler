import time
start = time.time()
first = 0
second = 1
third = 1
sums = 0
while third+second < 4000000:
    first = second
    second = third
    third = second + first
    if third%2==0:
        sums += third
print(sums)
print(time.time() - start)
