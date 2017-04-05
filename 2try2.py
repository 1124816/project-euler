import time
start = time.time()
one = 1
two = 2
sums = 0
while two < 4000000:
    sums +=two
    one = one+two
    two = one+two
    one = one+two
    two = one+two
    one = two-one
    two = two-one
    #two = one*2+two*3

print(sums)
print(time.time() - start)
