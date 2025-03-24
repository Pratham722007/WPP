def checksquare(a,b):
    count=0
    for i in range(a,b+1):
        if (int((i**0.5))**2==i):
            count+=1
    return count
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(checksquare(a,b))
