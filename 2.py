i=0
p=0
while i < 1000:
    if i%3==0:
        p+=i
    elif i%5==0:
        p+=i
    i+=1
print(p)
