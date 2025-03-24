n=int(input("ENTER A NUMBER : "))
sum=0
while n>0:
    q=n%10
    sum=sum*10+q
    n//=10
print(sum)
