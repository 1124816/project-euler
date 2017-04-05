all = 998001

def pal(num):
    return(str(num)[::-1] == str(num))

def loop():
    global all
    while True:
        if pal(all):
            p = 999
            while p >= 100:
                if all%p==0:
                    if all/p <=999 and all/p >=100:
                        return all
                p-=1
        all-=1
print(loop())
