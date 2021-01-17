def move(f,t):
    print("Move the disc from {} to {}!".format(f,t))


def hanoi(n,f,v,t):
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,v)
        move(f,t)
        hanoi(n-1,v,f,t)

hanoi(5,'A','B','C')

