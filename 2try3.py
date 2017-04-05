import time
start = time.time()
one = 1
two = 2
three = 2
sums = 0
while two < 4000000:
    sums +=two
    three = one*2+two*3
    one = one+two*2
    two = three

print(sums)
print(time.time() - start)
