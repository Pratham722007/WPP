def oddnum(n):
    p=(n-1)//2
    sum=0
    for i in range(p+1):
        sum=sum+2*i
    return sum


def evennum(n):
    return (n**2)//4
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n%2==0:
            print(evennum(n))
        else:
           print(oddnum(n)) 
main()
    

