def monsoon(num):
    return num*2
def summer(num):
    return num+1
t=int(input(("enter t : ")))
while(t!=0):

    n=int(input(("enter n : ")))
    result=0
    for i in range(0,n+1):
    
        if(i==0):
            result= 1
        elif(i%2==0):
            result=summer(result)
        else:
            result=monsoon(result)
    print(result)
    t-=1