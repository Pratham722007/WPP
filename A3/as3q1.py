def sumof(n):
    sum=0
    while(n>0):
        q=n%10
        sum=sum+q
        n=n//10
    return sum

def digitalroot(num):
    if(sumof(num)<10):
        return sumof(num)
    else:
        return digitalroot(sumof(num))

def main():
    num = int(input("Enter a number: "))
    print("Digital Root of the number is: ", digitalroot(num))
if(__name__=='__main__'):
    main()